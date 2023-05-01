# Python AWS Services Examples

This project provides examples of how to use various AWS services with Python and Boto3 library. The following services are covered:

    S3
    Lambda
    EC2
    SQS
    API Gateway HTTP API

Requirements

    Python 3.6 or higher
    Boto3 library
    AWS credentials with necessary permissions

List Operations Example

This example demonstrates how to manipulate a list in Python.

    list_example.py - This script creates an empty list and populates it with AWS services names. It then removes two specific services and prints the resulting list.

File Info Example

This example generates a list of dictionaries about files in the working directory and prints the list.

    file_info.py - This script retrieves information about files in the current directory and stores it in a list of dictionaries.

Stop EC2 Instances Example

This example shows how to stop all running EC2 instances in a region.

    stop_ec2_instances.py - This script retrieves all running EC2 instances in a region and stops them.

SQS and Lambda Example

This example shows how to send a message from a Lambda function to an SQS queue, and trigger the Lambda function using an API Gateway HTTP API.

    sqs_lambda.py - This script creates an SQS queue and a Lambda function. The Lambda function sends a message containing the current time or a random number to the SQS queue. The script also creates an API Gateway HTTP API trigger for the Lambda function and tests the trigger to verify the message was sent.

Contributing

Contributions are welcome! 
 
