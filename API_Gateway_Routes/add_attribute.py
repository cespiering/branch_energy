import requests
import json

url = "https://kw2p9xobpg.execute-api.us-west-1.amazonaws.com/add_attribute"

payload = json.dumps({
  "branch_id": "001",
  "field_name": "town",
  "field_value": "Houston"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
