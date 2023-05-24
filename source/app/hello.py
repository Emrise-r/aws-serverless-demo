import json

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
    "body": "{\r\n  \"key1\": \"hello -- world\",\r\n  \"key2\": \"value2\",\r\n  \"key3\": \"value3\"\r\n}",
    "isBase64Encoded": "false"
}

body = init_request.get('body', {})

print('body: {}, type: {}'.format(str(body), str(type(body))))
if not isinstance(body, dict):
    body = json.loads(body)
key = body.get('key1')
print("key1 value = " + key)
