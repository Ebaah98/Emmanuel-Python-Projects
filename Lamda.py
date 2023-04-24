import boto3
import json
import datetime
import dateutil.tz

# Create an SQS client
sqs = boto3.client('sqs')

# Specify the Queue URL
queue_url = 'https://sqs.us-east-1.amazonaws.com/282185981827/Week15'

# Lambda function handler
def lambda_handler(event, context):
    # Get the current time
    current_time = str(datetime.datetime.now())

    # Create a message dictionary
    message = {
        'current_time': current_time
    }

    # Send the message to the SQS Queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(message)
    )

    # Return a success response
    return {
        'statusCode': 200,
        'body': 'Message sent successfully - Let\'s go!'
    }Great job! It looks like you have successfully created a Lambda function that sends a message to an SQS queue and added an API Gateway trigger to it. Now it's time to test the trigger and confirm that the message was sent successfully.