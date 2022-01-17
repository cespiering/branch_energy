import requests

url = "https://kw2p9xobpg.execute-api.us-west-1.amazonaws.com/find_by_branch_id?branch_id=001&record_name=crm_id"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)