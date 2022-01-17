import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Branch_Home')

def new_branch_id(branch_id, crm_id):
    """Creates a new branch_id item in Table Branch_Home
    PARAMS: 
    branch_id: str
    crm_id: str
    RETURNS:
    String confirming new table item
    """
    with table.batch_writer() as batch:
        batch.put_item(Item={"branch_id": f"{branch_id}", "crm_id": f"{crm_id}" })
        return f"New branch_id: {branch_id} and crm_id: {crm_id} created"

def find_by_branch_id(branch_id, record_name):
    """Finds a record associated with branch_id
    PARAMS: 
    branch_id: str
    record_name: str
    RETURNS:
    record value: str 
    """
    resp = table.get_item(Key={'branch_id': f"{branch_id}"})
    return resp['Item'][f'{record_name}']

def create_new_field(branch_id, field_name, field_value):
    """Creates a new record field and value for branch_id
    PARAMS: 
    branch_id: str
    field_name: str
    field_value: str
    RETURNS:
    None 
    """
    resp = table.update_item(
    Key={"branch_id": f"{branch_id}"},
    
    ExpressionAttributeNames={
        "#field_name": f"{field_name}"
    },
    
    ExpressionAttributeValues={
        ":id": f"{field_value}",
    },
     UpdateExpression="SET #field_name = :id"
    )

    
def check_for_duplicates(branch_id, other_field=None):
    """checks for duplicate record names and values
    PARAMS: 
    branch_id: str
    other_field: str, optional
    RETURNS:
    bool 
    """
    resp = table.get_item(Key={"branch_id": f"{branch_id}"})
    existing_id = True
    if 'Item' not in resp.keys():
        return False
    if existing_id and other_field == None:
        return True
    if existing_id and other_field != None:
        #check for other_field in Item dict
        if other_field in resp['Item'].keys():
            return True
    return False
    
    