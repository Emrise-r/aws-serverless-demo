import json
from connect_dynamodb import connect_dynamodb
from respond import respond
from boto3.dynamodb.conditions import Attr

event = {
    "resource": "/query-data",
    "path": "/query-data",
    "httpMethod": "GET",
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "Host": "xudofheezh.execute-api.us-east-1.amazonaws.com",
        "Postman-Token": "40e77522-89f8-427f-83da-22e015c7c244",
        "User-Agent": "PostmanRuntime/7.32.2",
        "X-Amzn-Trace-Id": "Root=1-64645afc-392d851f37d3fe5c099405d1",
        "X-Forwarded-For": "222.252.26.224",
        "X-Forwarded-Port": "443",
        "X-Forwarded-Proto": "https"
    },
    "multiValueHeaders": {
        "Accept": [
            "*/*"
        ],
        "Accept-Encoding": [
            "gzip, deflate, br"
        ],
        "Content-Type": [
            "application/json"
        ],
        "Host": [
            "xudofheezh.execute-api.us-east-1.amazonaws.com"
        ],
        "Postman-Token": [
            "40e77522-89f8-427f-83da-22e015c7c244"
        ],
        "User-Agent": [
            "PostmanRuntime/7.32.2"
        ],
        "X-Amzn-Trace-Id": [
            "Root=1-64645afc-392d851f37d3fe5c099405d1"
        ],
        "X-Forwarded-For": [
            "222.252.26.224"
        ],
        "X-Forwarded-Port": [
            "443"
        ],
        "X-Forwarded-Proto": [
            "https"
        ]
    },
    "queryStringParameters": "null",
    "multiValueQueryStringParameters": {
        "Userid": [
            "aaaaa"
        ],
    },
    "pathParameters": "null",
    "stageVariables": "null",
    "requestContext": {
        "resourceId": "ygt1yl",
        "resourcePath": "/query-data",
        "httpMethod": "GET",
        "extendedRequestId": "FDMnjHzYoAMFmGA=",
        "requestTime": "17/May/2023:04:41:32 +0000",
        "path": "/default/query-data",
        "accountId": "942408480634",
        "protocol": "HTTP/1.1",
        "stage": "default",
        "domainPrefix": "xudofheezh",
        "requestTimeEpoch": "1684298492834",
        "requestId": "c17a2f67-91b5-4d05-9bfb-11950c7bd833",
        "identity": {
            "cognitoIdentityPoolId": "null",
            "accountId": "null",
            "cognitoIdentityId": "null",
            "caller": "null",
            "sourceIp": "222.252.26.224",
            "principalOrgId": "null",
            "accessKey": "null",
            "cognitoAuthenticationType": "null",
            "cognitoAuthenticationProvider": "null",
            "userArn": "null",
            "userAgent": "PostmanRuntime/7.32.2",
            "user": "null"
        },
        "domainName": "xudofheezh.execute-api.us-east-1.amazonaws.com",
        "apiId": "xudofheezh"
    },
    "body": "{\r\n    \"people\": [\r\n        {\"userid\": \"QXoxqO\", \"name\": \"Vinh\"},\r\n        {\"userid\": \"54skaDT\", \"name\": \"Sang\"},\r\n        {\"userid\": \"UnZff8TG\", \"name\": \"Thanh\"}\r\n    ]\r\n            \r\n}",
    "isBase64Encoded": "false"
}


def lambda_handler(event, context):
    table_name = 'serverless_test_table'
    dynamodb = connect_dynamodb()
    table = dynamodb.Table(table_name)
    result = None
    print("context:", json.dumps(context) )
    print("event:", json.dumps(event), 'type:', type(event))
    queryStringParameters = event['queryStringParameters']
    print("queryStringParameters:", json.dumps(queryStringParameters), 'type:', type(queryStringParameters))
    if queryStringParameters is None | queryStringParameters['name'] is None:
        name = ''
    else:
        name = queryStringParameters['name']
        print("Name:", json.dumps(name), 'type:', type(name))
    result = table.scan(FilterExpression=Attr('Name').contains(name))
    print(result)
    return respond(None, result)


lambda_handler(event, None)
