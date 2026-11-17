from .ledger import movement_balances,transfer_details
from .storage import records


def overview(connection):
    return {'movements':movement_balances(connection),'transfers':transfer_details(connection),
            'counts':records(connection,'SELECT * FROM counts ORDER BY count_id')}
