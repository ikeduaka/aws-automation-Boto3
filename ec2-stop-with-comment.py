import boto3

# stopping all instances in every department

ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
    instance.stop()
    