import zipfile
import boto3
import os
import json
import time


def create_lambda_role():
    lambda_client_iam = boto3.client("iam")

    # Define the trust policy for the role
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "lambda.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }

    # Create the role
    role_response = lambda_client_iam.create_role(
        RoleName='my-lambda-role',
        AssumeRolePolicyDocument=json.dumps(trust_policy)
    )

    # Define the permissions policy for the role
    permissions_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "logs:CreateLogGroup",
                "Resource": "arn:aws:logs:us-east-1:{}:*".format(ACCOUNT_ID)
            },
            {
                "Effect": "Allow",
                "Action": [
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],
                "Resource": [
                    "arn:aws:logs:us-east-1:{}:log-group:/aws/lambda/{}:*".format(ACCOUNT_ID, FUNCTION_NAME)
                ]
            }
        ]
    }

    # Attach the permissions policy to the role
    lambda_client_iam.put_role_policy(
        RoleName='my-lambda-role',
        PolicyName='my-lambda-policy',
        PolicyDocument=json.dumps(permissions_policy)
    )

    return role_response['Role']['Arn']


def delete_lambda_iam_role(role_name):
    lambda_client_iam = boto3.client("iam")
    lambda_client_iam.delete_role(
        RoleName=role_name
    )


def delete_lambda_iam_policy(role_name, policy_name):
    lambda_client_iam = boto3.client("iam")
    lambda_client_iam.delete_role_policy(
        RoleName=role_name,
        PolicyName=policy_name
    )


def create_lambda_function(function_name, role_name):
    lambda_client = boto3.client("lambda")

    with open("lambda_code.zip", mode="rb") as archive:
        response = lambda_client.create_function(
            Code={
                'ZipFile': archive.read()
            },
            Description='API that respond Hello World',
            FunctionName=function_name,
            Handler='lambda_handler',
            MemorySize=128,
            Publish=True,
            Role=role_name,
            Runtime='python3.10',
            Timeout=15
        )
        print(response)


def delete_lambda_function(function_name):
    lambda_client = boto3.client("lambda")

    lambda_client.delete_function(
        FunctionName=function_name
    )


def zip_code():
    with zipfile.ZipFile("lambda_code.zip", mode="w") as archive:
        archive.write("lambda_function.py")


if __name__ == "__main__":
    ACCOUNT_ID = os.getenv("ACCOUNT_ID")
    FUNCTION_NAME = "my-function-hello"

    # Zip Code files
    zip_code()

    # Create role to execute lambda function
    lambda_role_arn = create_lambda_role()
    time.sleep(10)

    # Create and publish the function
    create_lambda_function(FUNCTION_NAME, lambda_role_arn)
    time.sleep(10)

    # Delete function
    delete_lambda_function(FUNCTION_NAME)

    # Delete role and policy
    delete_lambda_iam_policy('my-lambda-role', 'my-lambda-policy')
    delete_lambda_iam_role('my-lambda-role')
