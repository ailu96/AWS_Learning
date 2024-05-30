import json
from datetime import datetime
def purchaseOrder(event, context):
    # TODO implement
    
    print('The data is:',event['TransactionType'])
    
    return {
        
        'transactionType': event['TransactionType'],
        'message':'Hello from Purchase Order',
        'timestamp':datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
