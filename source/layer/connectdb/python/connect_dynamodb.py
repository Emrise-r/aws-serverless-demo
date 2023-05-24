import boto3


def connect_dynamodb(): return boto3.resource('dynamodb')
