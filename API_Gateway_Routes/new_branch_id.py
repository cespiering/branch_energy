import requests
import json

url = "https://kw2p9xobpg.execute-api.us-west-1.amazonaws.com/new_branch_id"

payload = json.dumps({
  "branch_id": "001",
  "crm_id": "000"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
