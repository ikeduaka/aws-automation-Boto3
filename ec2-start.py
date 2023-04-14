import boto3


ec2 = boto3.resource('ec2')



instances = ec2.create_instances(
ImageId="ami-06e46074ae430fba6",
InstanceType="t2.micro",
MaxCount=1,
MinCount=1,

TagSpecifications=[
   {
      "ResourceType":'instance',
      "Tags":[
         {
            "Key":"Name",
            "Value":"prod_server"
         }
      ]
   }
 ]
)

print(instances)
