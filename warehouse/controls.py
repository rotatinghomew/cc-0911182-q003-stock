from .ledger import movement_balances,transfer_details
from .storage import digest,records,transaction


def audit_stock(connection):
    issues=[]
    for balance in movement_balances(connection):
        if balance['negative']:
            issues.append({'warehouse':balance['warehouse'],'sku':balance['sku'],'reason':'普通流水为负','quantity':str(balance['movement_quantity'])})
    for transfer in transfer_details(connection):
        if transfer['over_received']:
            issues.append({'warehouse':transfer['destination'],'sku':transfer['sku'],'reason':'验收超过发出数量','quantity':str(transfer['accounted_quantity']-transfer['quantity'])})
    ids={row[0] for row in connection.execute('SELECT transfer_id FROM transfers').fetchall()}
    for arrival in records(connection,'SELECT * FROM arrivals ORDER BY arrival_id'):
        if arrival['transfer_id'] not in ids:
            issues.append({'warehouse':'unknown','sku':'unknown','reason':'验收没有调拨原单','quantity':str(arrival['quantity'])})
    with transaction(connection):
        connection.execute('DELETE FROM stock_alerts')
        for issue in issues:
            connection.execute('INSERT INTO stock_alerts VALUES (?,?,?,?,?)',[digest(issue),issue['warehouse'],issue['sku'],issue['reason'],issue['quantity']])
    return issues
