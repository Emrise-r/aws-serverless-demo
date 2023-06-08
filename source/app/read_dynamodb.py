import json
from connect_dynamodb import connect_dynamodb
from respond import respond

event = {
    "version": "2.0",
    "routeKey": "GET /users/{id}",
    "rawPath": "/rwx/users/QXoxqO",
    "rawQueryString": "",
    "headers": {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "content-length": "0",
        "host": "29x1im9jfl.execute-api.us-east-1.amazonaws.com",
        "postman-token": "02391cfb-1ce3-44bb-abf5-ae3d8c668d94",
        "user-agent": "PostmanRuntime/7.32.2",
        "x-amzn-trace-id": "Root=1-64644421-7f2645364586f22336b398a9",
        "x-forwarded-for": "222.252.26.224",
        "x-forwarded-port": "443",
        "x-forwarded-proto": "https"
    },
    "requestContext": {
        "accountId": "942408480634",
        "apiId": "29x1im9jfl",
        "domainName": "29x1im9jfl.execute-api.us-east-1.amazonaws.com",
        "domainPrefix": "29x1im9jfl",
        "http": {
            "method": "GET",
            "path": "/rwx/users/QXoxqO",
            "protocol": "HTTP/1.1",
            "sourceIp": "222.252.26.224",
            "userAgent": "PostmanRuntime/7.32.2"
        },
        "requestId": "FC-VOglRoAMEJjA=",
        "routeKey": "GET /users/{id}",
        "stage": "rwx",
        "time": "17/May/2023:03:04:01 +0000",
        "timeEpoch": "1684292641189"
    },
    "pathParameters": {
        "id": "QXoxqO"
    },
    "isBase64Encoded": "false"
}


def lambda_handler(event, context):
    table_name = 'serverless_test_table'
    dynamodb = connect_dynamodb()
    table = dynamodb.Table(table_name)
    result = None
    # print("context:", json.dumps(context) )
    print("event:", json.dumps(event), 'type:', type(event))
    pathParameters = event['pathParameters']
    print("pathParameters:", json.dumps(pathParameters), 'type:', type(pathParameters))
    id = pathParameters['id']
    print("id:", json.dumps(id), 'type:', type(id))
    key = {
        'id': id
    }
    result = table.get_item(Key=key)
    print(result)
    return result


lambda_handler(event, None)
