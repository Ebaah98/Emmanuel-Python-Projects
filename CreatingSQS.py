# Import the Boto3 library
import boto3

# Connect to the SQS
sqs = boto3.resource('sqs')

# Set name of the queue
queue_name = 'Week15'

# Create the queue
queue = sqs.create_queue(QueueName=queue_name)

# Print the URL of the queue
print(queue.url)