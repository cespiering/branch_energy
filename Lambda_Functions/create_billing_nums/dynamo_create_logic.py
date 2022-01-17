import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
billing_table = dynamodb.Table('Billing_Nums')
branch_table = dynamodb.Table('Branch_Home')


def check_for_duplicate_billing_num(billing_num):
    """Checks for duplicate billing_num in Billing_Nums table
    PARAMS: 
    billing_num: str
    RETURNS:
    bool
    """
    response = billing_table.get_item(Key={'billing_num': f"{billing_num}"})
    if 'Item' not in response.keys():
        return False
    return True


def create_branch_table_record(branch_id, billing_num):
    """adds billing_num to branch_id, or creates billing_num list if none exists
    PARAMS: 
    branch_id: str
    billing_num: str
    RETURNS:
    nothing, or error message if error
    """
    try:
        branch_table.update_item(
            Key = {"branch_id": f"{branch_id}"},
            ExpressionAttributeValues= {
                ":id" : [billing_num]
            },
            UpdateExpression="set billing_num = list_append(billing_num, :id)"
        )

    except ClientError as e:
        if e.response['Error']['Code'] == 'ValidationException':
            branch_table.update_item(
                Key={"branch_id": f"{branch_id}"},
                UpdateExpression="set #attrName = :attrValue",
                ExpressionAttributeNames = {
                    "#attrName" : "billing_num"
                },
                ExpressionAttributeValues={
                    ':attrValue': [billing_num]
                },
            )
    except:
        return "Billing number or branch_id not valid"

 
def create_billing_table_record(branch_id, billing_num):
    """Creates a new branch_id item in Billing_Nums Table 
    PARAMS: 
    branch_id: str
    billing_num: str
    RETURNS:
    nothing, or error message if error
    """
    try:
        billing_table.put_item(Item={ "billing_num": f"{billing_num}", "branch_id": f"{branch_id}" })
    except:
        return "Billing number or branch_id not valid"
        
        
def create_all_billing_records(branch_id, billing_num):
    """Manages all functions for billing_num creation in both tables
    PARAMS: 
    branch_id: str
    billing_num: str
    RETURNS:
    message indicating success or failure
    """
    duplicate = check_for_duplicate_billing_num(billing_num)
    if not duplicate:
        create_billing_table_record(branch_id, billing_num)
        create_branch_table_record(branch_id, billing_num)
        return f"Billing number {billing_num} attached to branch_id {branch_id}"
    else:
        return "This billing number already exists"
