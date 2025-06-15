import boto3
import zipfile
import os
import time

# Constants
app_name = 'my-eb-python-app'
env_name = 'my-eb-python-env'
version_label = f'version-{int(time.time())}'
s3_bucket = 'your-s3-bucket-name'
zip_file = 'app.zip'
region = 'us-east-1'  # Change to your preferred AWS region

# Initialize clients
eb = boto3.client('elasticbeanstalk', region_name=region)
s3 = boto3.client('s3', region_name=region)

# Upload app.zip to S3
s3.upload_file(zip_file, s3_bucket, zip_file)

# Create application version
response = eb.create_application_version(
    ApplicationName=app_name,
    VersionLabel=version_label,
    Description='Deployed from boto3 script',
    SourceBundle={
        'S3Bucket': s3_bucket,
        'S3Key': zip_file
    },
    Process=True
)

print(f"Created application version: {version_label}")

# Check if environment exists
envs = eb.describe_environments(ApplicationName=app_name)['Environments']
existing_env = next((e for e in envs if e['EnvironmentName'] == env_name), None)

if existing_env:
    # Update existing environment
    eb.update_environment(
        EnvironmentName=env_name,
        VersionLabel=version_label
    )
    print(f"Updated environment: {env_name}")
else:
    # Create new environment
    eb.create_environment(
        ApplicationName=app_name,
        EnvironmentName=env_name,
        SolutionStackName='64bit Amazon Linux 2 v3.5.7 running Python 3.8',
        VersionLabel=version_label,
        OptionSettings=[
            {
                'Namespace': 'aws:elasticbeanstalk:environment',
                'OptionName': 'EnvironmentType',
                'Value': 'SingleInstance'
            }
        ]
    )
    print(f"Created new environment: {env_name}")
