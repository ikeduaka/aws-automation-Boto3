import boto3

# SDK for interaction between AWS and Python

sqs = boto3.client('sqs')

# Creating a SQS queue
response = sqs.create_queue(
    QueueName='store_time')

# Get URL for SQS queue
response = sqs.get_queue_url(QueueName='store_time')

print(response['QueueUrl'])
