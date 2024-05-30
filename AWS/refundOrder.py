import json
from datetime import datetime
def refundOrder(event, context):
    # TODO implement
    
    print('The data is:',event['TransactionType'])
    # Convert datetime to string
    
    return {
        
        'transactionType': event['TransactionType'],
        'message':'Hello from Refund Order',
        'timestamp':datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
