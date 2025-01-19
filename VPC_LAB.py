# Create VPC  by navigate to EC2 , Client , CreateVPC()
import boto3
from pprint import pprint

vpc_session=boto3.session.Session()
vpc_obj=vpc_session.client(service_name='ec2',region_name='us-east-1')

''''''
#response = vpc_obj.create_vpc(
#    CidrBlock='10.10.10.0/24',
# )

#request01=response['ResponseMetadata']
#pprint(response)
''''''
response = vpc_obj.describe_vpcs()

#pprint(response)

for item in response['Vpcs']:
    pprint ( f'this is the list of VPCs ID {item["VpcId"]} AND {item["CidrBlock"]}')

