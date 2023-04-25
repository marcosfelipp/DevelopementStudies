import json
import boto3
import os

print("loading function...")
region_name = os.environ['REGION_NAME']
dynamo = boto3.client("dynamodb", region_name=region_name)
table_name = os.environ['TABLE_NAME']


def lambda_handler(event, context):
    """Sample pure Lambda function
    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format
        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
    context: object, required
        Lambda Context runtime methods and attributes
        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html
    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict
        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    scan_result = dynamo.scan(TableName=table_name)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": scan_result,
        }),
    }