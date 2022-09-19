import requests
import json

baseURL = "https://api.meraki.com/api/v1"
headers = {'X-Cisco-Meraki-API-Key': 'e97901f4899d7db137e3d0265d480b8b599247ff'}
organizations = "/organizations"
networks = "/networks"
orgid = "/549236"
nid = ""

response = requests.get((baseURL + organizations + orgid + networks), headers=headers)

print(response.text)