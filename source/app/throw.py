import json

from handle import handle_exception
from handle import CustomException
from respond import respond


def lamda_handle(event, context):
    result = handle_exception(throw_func, event=event)
    if isinstance(result, Exception):
        return respond(result, None)
    else:
        return respond(None, result)


def throw_func(**kwargs):
    event = kwargs['event']
    number = json.loads(event['body'])['number']
    if number < 0:
        raise Exception("unknow number")
    elif number % 2 == 0:
        return number
    else:
        raise CustomException(message="not prime")


event = {
    "body": "{\r\n  \"aaa\": -3 \r\n}"
}


response = lamda_handle(event, None)

print("response:", json.dumps(response))
