import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Billing_Nums')

def find_by_billing_num(billing_num):
    """Finds branch_id associated with billing_num
    PARAMS: 
    billing_num: str
    RETURNS:
    branch_id: str
    """    
    resp = table.get_item(Key={'billing_num': f"{billing_num}"})
    return resp['Item']['branch_id']