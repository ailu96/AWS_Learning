import json

def resultHandler(event, context):
    # TODO implement
    return {
        'Result' :event['message']
    }
