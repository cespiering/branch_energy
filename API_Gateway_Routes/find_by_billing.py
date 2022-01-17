import requests

url = "https://kw2p9xobpg.execute-api.us-west-1.amazonaws.com/find_by_billing?billing_num=001"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
