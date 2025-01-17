import boto3
from pprint import pprint 

# 1- Create  Session Object with EC2  $  Service Name is required to add it 

ec2_session=boto3.session.Session()
client_obj=ec2_session.client(service_name='ec2' , region_name='us-east-1')
# 2- Create EC2  Instance

EC_Instance_Run = client_obj.run_instances(
   
    ImageId='ami-04b4f1a9cf54c11d0',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
    
)

# To extract Instance ID , use the following 

instance_id = EC_Instance_Run['Instances'][0]['InstanceId']


pprint(f' Instance id is {instance_id}')