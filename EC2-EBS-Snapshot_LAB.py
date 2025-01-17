import boto3
from pprint import pprint

# 1- Create client session for EC2
EC2_Session = boto3.session.Session()
client_obj = EC2_Session.client(service_name='ec2', region_name='us-east-1')

# 2- Create EC2 Instance
EC2_Instance_Run = client_obj.run_instances(
    ImageId='ami-04b4f1a9cf54c11d0',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
)

# 3- Extract EC2 Instance ID
EC2_Instance_ID = EC2_Instance_Run['Instances'][0]['InstanceId']

# 4- Configure Waiter to wait until EC2 is running
waiter = client_obj.get_waiter('instance_running')
waiter.wait(InstanceIds=[EC2_Instance_ID])

# 5- Describe Volume ID attached to the instance
volume_describe = client_obj.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [
                EC2_Instance_ID,
            ]
        },
    ],
)

# 6- Extract Volume ID
volume_id = volume_describe['Volumes'][0]['VolumeId']
pprint(f'Volume ID: {volume_id}')

# 7- Create Snapshot from the EBS volume
ebs_snapshot = client_obj.create_snapshot(
    Description='EBS_Snapshot',
    VolumeId=volume_id
)

# Print snapshot information
pprint(f'Snapshot created: {ebs_snapshot["SnapshotId"]}')
