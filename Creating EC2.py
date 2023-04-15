import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-06e46074ae430fba6',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=2,
    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name','Value':'EmmanuelEnv'}]}]
)

print(instance)