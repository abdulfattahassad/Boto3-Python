import boto3
import boto3.session
from pprint import pprint

# To check Boto3 Documentation , Go to "Available Service" Section as below
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html
 
# 1- Create Session Object 
IAM_Session=boto3.session.Session()

# Create iam as client object  as per doc 
# client = boto3.client('iam')  --> this command require some changes like replace boto3 with IAM_Session 

client_obj=IAM_Session.client('iam')

# 2- Create the user 
boto3_client03_var="boto3_client03"
response = client_obj.create_user(UserName='boto3_client03_var') 

# 3- Create Access key   ## instead of type username every time , put it in variable
client_access_keys = client_obj.create_access_key(UserName='boto3_client03_var')
pprint(client_access_keys)
# to catch access keys and secret keys  use the following :


access_keys_id=client_access_keys['AccessKey']['AccessKeyId']
access_secret_keys=client_access_keys['AccessKey']['SecretAccessKey']

# 4- Attach user Policy 

user_policy = client_obj.attach_user_policy(
    UserName='boto3_client02_var',
    PolicyArn='arn:aws:iam::aws:policy/AmazonEC2FullAccess'
)

print (f" the user {boto3_client03_var} has been created with access_keys{access_keys_id} and secret_keys {access_secret_keys}")