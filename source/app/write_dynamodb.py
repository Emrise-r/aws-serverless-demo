import json
import uuid

from respond import respond
from connect_dynamodb import connect_dynamodb


print('Loading function')


def lambda_handler(event, context):
    table_name = 'serverless_test_table'
    dynamodb = connect_dynamodb()
    table = dynamodb.Table(table_name)
    result = None
    payload = json.loads(event['body'])
    print("Payload:", json.dumps(payload), 'type:', type(payload))
    people = payload['people']
    print("Payload: ", json.dumps(people), 'type:', type(people))
    # with table.batch_writer() as batch_writer:
    # batch_writer = table.batch_writer()
    for person in people:
        item = {
            '_id': uuid.uuid4().hex,
            'Userid': person['userid'],
            'FullName': person['name']
        }
        print("> batch writing: {}".format(person['userid']))
        try:
            table.put_item(Item=item)
        except Exception as e:
            print("Error Excuse batch, Trace: {}".format(e))
    result = f"Success. Added {len(people)} people to {table_name}."
    print(result)
    return respond(None, result)


init_request = {
    "version": "2.0",
    "routeKey": "ANY /hello-world-admin",
    "rawPath": "/hello-world-admin",
    "rawQueryString": "",
    "headers": {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "content-length": "74",
        "content-type": "application/json",
        "host": "5wxm53ccb2.execute-api.us-east-1.amazonaws.com",
        "postman-token": "1e25eece-6cee-46d7-8240-5f07ef41666a",
        "user-agent": "PostmanRuntime/7.32.2",
        "x-amzn-trace-id": "Root=1-645b83a1-597e469916e14c4706a86ade",
        "x-forwarded-for": "222.252.26.224",
        "x-forwarded-port": "443",
        "x-forwarded-proto": "https"
    },
    "requestContext": {
        "accountId": "942408480634",
        "apiId": "5wxm53ccb2",
        "domainName": "5wxm53ccb2.execute-api.us-east-1.amazonaws.com",
        "domainPrefix": "5wxm53ccb2",
        "http": {
            "method": "POST",
            "path": "/hello-world-admin",
            "protocol": "HTTP/1.1",
            "sourceIp": "222.252.26.224",
            "userAgent": "PostmanRuntime/7.32.2"
        },
        "requestId": "EtGBTihBIAMEPMg=",
        "routeKey": "ANY /hello-world-admin",
        "stage": "$default",
        "time": "10/May/2023:11:44:33 +0000",
        "timeEpoch": 1683719073602
    },
    "body": "{\r\n    \"people\": [\r\n        {\"userid\": \"J5bSiw\", \"name\": \"Vinh\"},\r\n        {\"userid\": \"fpAsq9T\", \"name\": \"Sang\"},\r\n        {\"userid\": \"PzEh7dvM\", \"name\": \"Thanh\"}\r\n    ]\r\n            \r\n}",
    "isBase64Encoded": "false"
}

lambda_handler(init_request, None)
