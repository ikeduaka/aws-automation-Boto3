import boto3

# Region locator and input tag to create department as required

def create_apache_ec2(client, MaxCount=1, MinCount=1, KeyName=None, tag=None):
    region = client.meta.region_name
    
    amis = {"us-east-1":"ami-06e46074ae430fba6"}
    
    x = input("What's your tag name: ")
    
    try:
        ami = amis[region]
    except:
        print("Region not supported")
        return None
    
 # creating ec2 instances to each specifc department (dev, prod, acc)   
    try:
        if (KeyName=="New-3tier-key" and x =="prod_server"):
            client.run_instances(MaxCount=MaxCount,
                         MinCount=MinCount,
                         ImageId=ami,
                         InstanceType="t2.micro",
                         TagSpecifications=[
                         {"ResourceType":'instance',
                          "Tags":[
                          {"Key":"Name",
                          "Value":"prod_server"}]}])
                          
        elif (KeyName=="New-3tier-key" and x =="dev_server"):  
            client.run_instances(MaxCount=MaxCount,
                         MinCount=MinCount,
                         ImageId=ami,
                         InstanceType="t2.micro",
                         TagSpecifications=[
                         {"ResourceType":'instance',
                          "Tags":[
                          {"Key":"Name",
                          "Value":"dev_server"}]}])
        
        elif (KeyName=="New-3tier-key" and x =="acc_server"):
            client.run_instances(MaxCount=MaxCount,
                         MinCount=MinCount,
                         ImageId=ami,
                         InstanceType="t2.micro",
                         TagSpecifications=[
                         {"ResourceType":'instance',
                          "Tags":[
                          {"Key":"Name",
                          "Value":"acc_server"}]}])
        else:
            print("user_name doesn't exist")
                             
        print("Started")
    except Exception as e:
        print("Failed", e)
    
if __name__ == "__main__":
    client = boto3.client('ec2')
    
    create_apache_ec2(client, KeyName="New-3tier-key")