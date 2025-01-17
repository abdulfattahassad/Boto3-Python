## TO list all EC2 , Go to Client Object--> describe methods
import boto3
from pprint import pprint

# 1- Create Session with EC2 

client_obj=boto3.session.Session()
EC2_List=client_obj.client(service_name='ec2',region_name='us-east-1')

# 2- get all EC2 List
response = EC2_List.describe_instances()
#pprint(response)
for instance_id in  response['Reservations']:
    for instances_id_result in instance_id['Instances']:
        pprint( instances_id_result['InstanceId'])


