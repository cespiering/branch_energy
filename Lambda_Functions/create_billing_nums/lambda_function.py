import json
from dynamo_create_logic import create_all_billing_records

def lambda_handler(event, context):
    body = json.loads(event["body"])
    branch_id = body["branch_id"]
    billing_num = body["billing_num"]
    response = create_all_billing_records(branch_id, billing_num)
    return response
