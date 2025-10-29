Remove all unneccesary feilds and keep required fields such as star marked.

to see req feilds go to create in space where description, summary, worktype are mandatory

for issue version id:

board > ... > configure board > worktype > story > id will be on url like 10009

change project id to key and add your project key ex. SID

import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://sab-jan.atlassian.net/rest/api/3/issue"

API_TOKEN = " yoour jira tocken"
auth = HTTPBasicAuth("sab.jan.02.2001@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "this is a sample issue",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10009"
    },
    "project": {
      "key": "SID"
    },
    "summary": "Jira ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
