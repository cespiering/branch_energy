# Creating the main branch_id table

import boto3

client = boto3.client('dynamodb')

try:
    resp = client.create_table(
        TableName="Branch_Home",
        KeySchema=[
            {
                "AttributeName": "branch_id",
                "KeyType": "HASH"
            },
           
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "branch_id",
                "AttributeType": "S"
            },
            
        ],
        # ProvisionedThroughput controls the amount of data you can read or write to DynamoDB per second.
        # You can control read and write capacity independently.
        ProvisionedThroughput={
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        }
    )
    print("Table created successfully!")
except Exception as e:
    print("Error creating table:")
    print(e)
