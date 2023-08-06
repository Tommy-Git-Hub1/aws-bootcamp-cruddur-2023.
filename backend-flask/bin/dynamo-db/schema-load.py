#!/usr/bin/env python3
import boto3
import sys

attrs = {'endpoint_url':'http://localhost:8000'}


if len(sys.argv) == 2:
  if "prod" == sys.argv[1]:
    attrs = {}

dynamodb=boto3.client("dynamodb", **attrs)
table_name= 'cruddur-message'

response = dynamodb.create_table(
    TableName= table_name,
    AttributeDefinitions=[
        {
            'AttributeName': 'pk', #Partition key
            'AttributeType': 'S' #string
        },
        {
            'AttributeName': 'sk', #Secondary/Sort key
            'AttributeType': 'S' #string
        },
    ],
    
    KeySchema=[
        {
            'AttributeName': 'pk',
            'KeyType': 'HASH' #For partition Key
        },
        {
            'AttributeName': 'sk',
            'KeyType': 'RANGE' #For partition Key
        },
    ],
   
    #GlobalSecondaryIndexes=[
    #],
    BillingMode='PROVISIONED',
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    },
   
)
print(response)