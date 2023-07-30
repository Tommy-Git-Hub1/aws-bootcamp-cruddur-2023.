#!/usr/bin/env python3

import boto3
import sys

attrs = {'endpoint_url':'http://localhost:8000'}
dynamodb=boto3.client("dynamodb", **attrs)

response = dynamodb.list_tables(
    ExclusiveStartTableName='string',
    Limit=5
)

print(response)