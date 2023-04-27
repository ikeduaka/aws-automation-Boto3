import boto3
from datetime import datetime
import json

# Create SQS client
sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-east-1.amazonaws.com/603747066203/store_queue'

# Send message to SQS queue

def lambda_handler(event, context):
    now = datetime.now()
    current_date = datetime.now()
    current_date_time = now.strftime("%d/%m/%Y %H:%M:%S")

    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=(
        'Information about my current date and times.'))
        
        
    return {
    'statusCode': 200,
    'body': json.dumps(current_date_time)
    }

