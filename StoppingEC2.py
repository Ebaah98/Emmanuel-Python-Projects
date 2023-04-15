import boto3

ec2 = boto3.resource('ec2')
tag = {'Name':'tag:Name','Values':['Emanuel-Development-lap']}

instances = ec2.instances.filter(Filters=[tag])

for instance in instances:
    instance.stop()
    print("DONE")
    
    