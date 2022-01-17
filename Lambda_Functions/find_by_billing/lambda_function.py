import json

from dynamo_billing_logic import find_by_billing_num
    

def lambda_handler(event, context):
    try:
        billing_num = event["queryStringParameters"]['billing_num']
        branch_id = find_by_billing_num(billing_num)
        return f"The branch_id is {branch_id}"
    except KeyError:
        return "No such record exists"

