import requests
import json

url = "https://kw2p9xobpg.execute-api.us-west-1.amazonaws.com/create_billing_num"

payload = json.dumps({
  "branch_id": "001",
  "billing_num": "001"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)