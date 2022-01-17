import json

from dynamo_logic import find_by_branch_id, new_branch_id, create_new_field, check_for_duplicates

NEW_BRANCH_ID = '/new_branch_id'
FIND_BRANCH_ID = '/find_by_branch_id'
CREATE_NEW_FIELD = '/add_attribute'



def lambda_handler(event, context):
    print(event)

    if event['rawPath'] == FIND_BRANCH_ID:
        try:
            branch_id = event["queryStringParameters"]['branch_id']
            record_name = event["queryStringParameters"]['record_name']
            record_value = find_by_branch_id(branch_id, record_name)
            return f"{record_name}: {record_value}"
        except KeyError:
            return "No such record exists"

    else:
        body = json.loads(event["body"])
        branch_id = body["branch_id"]
        
        if event['rawPath'] == NEW_BRANCH_ID:
            try:
                duplicate_branch_id = check_for_duplicates(branch_id)
                if not duplicate_branch_id:
                    crm_id = body["crm_id"]
                    return new_branch_id(branch_id, crm_id)
                else:
                    return "This branch id already exists"
            except KeyError:
                return "KeyError"
            except:
                return "something went wrong"

        elif event['rawPath'] == CREATE_NEW_FIELD:
            try:
                field_name = body["field_name"]
                field_value = body["field_value"]
                duplicate_record = check_for_duplicates(branch_id, field_name)
                
                if not duplicate_record:
                    create_new_field(branch_id, field_name, field_value)             
                    return f"New field: {field_name} created for branch_id: {branch_id}"
                else:
                    return f"There is already a record field named {field_name}"
            except KeyError:
                return "Not enough info"