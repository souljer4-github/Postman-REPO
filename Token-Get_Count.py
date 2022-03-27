import requests
import json
import requests
from getpass import getpass
import json
from pprint import pprint
from requests.auth import HTTPBasicAuth
user = input("Please provide your DNAC username: ")

password = getpass("Please provide your DNAC password: ")

BASEURL = "https://sandboxdnac.cisco.com"
TOKENURL = "/dna/system/api/v1/auth/token"
DEVICEAPIURL = "/dna/intent/api/v1/network-device"
DNACAuth = BASEURL + TOKENURL
DNACDEVICEURL = BASEURL + DEVICEAPIURL


payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.post(DNACAuth, auth=HTTPBasicAuth(user, password), headers=headers, data=payload)
tokenjson = response.json()
TOKEN = tokenjson["Token"]
pprint('Your Token has been successfully generated. The value of your toke is: \n' + TOKEN)



url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-Auth-Token': TOKEN,
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.request("GET", url, headers=headers, data=payload)


pprint(response.text)

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device/count"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-Auth-Token': TOKEN
}

response = requests.request("GET", url, headers=headers, data=payload)
print("\n")
print(response.text)
