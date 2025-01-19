from pprint import pprint 
#The os module in Python provides a way to interact with the operating system. It includes functions to handle file operations, environment variables, process management, and other system-level functionalities.

#Some key features of the os module include:

#Environment Variables: You can access and modify environment variables in the operating system.
#Lambda functions often use environment variables to store sensitive information (e.g., API keys, database credentials, configuration settings) without hardcoding them into the code. The os module is used to access these environment variables.

import os

def lambda_handler(event, context):
    # Access environment variable
    db_password = os.getenv('DB_PASSWORD')
    print(f"Database password is: {db_password}")

pprint (dir(os))
