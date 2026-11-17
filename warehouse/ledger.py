from decimal import Decimal
from .storage import records


def movement_balances(connection):
    rows=records(connection,'SELECT m.*,p.pack_size FROM movements m LEFT JOIN products p USING(sku) ORDER BY movement_id')
    balances={}
    for row in rows:
        if row['pack_size'] is None:
            raise ValueError('商品包装未知')
        multiplier=row['pack_size'] if row['unit']=='box' else Decimal(1)
        key=(row['warehouse'],row['sku'])
        balances[key]=balances.get(key,Decimal(0))+row['quantity']*multiplier
    return [{'warehouse':key[0],'sku':key[1],'movement_quantity':value,'negative':value<0} for key,value in sorted(balances.items())]


def transfer_details(connection):
    result=[]
    for transfer in records(connection,'SELECT * FROM transfers ORDER BY transfer_id'):
        rows=records(connection,'SELECT * FROM arrivals WHERE transfer_id=? ORDER BY arrival_id',[transfer['transfer_id']])
        transfer['arrivals']=rows
        transfer['accounted_quantity']=sum((row['quantity'] for row in rows),Decimal(0))
        transfer['over_received']=transfer['accounted_quantity']>transfer['quantity']
        result.append(transfer)
    return result
