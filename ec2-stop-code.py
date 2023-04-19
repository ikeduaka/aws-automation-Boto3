import boto3

region = 'us-east-1'

ec2 = boto3.resource("ec2", region_name=region)


instances = ec2.instances.filter(
    Filters = [{'Name': 'instance-state-name', 'Values': ['running']},
    {'Name':'tag:Name', 'Values':['prod_server']}]
    )
    
for instance in instances:
    try:
        instance.stop()
        print(f'{instance} stopped')
        
    except:
        print(f'Error stopping {instances}')