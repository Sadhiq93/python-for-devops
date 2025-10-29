let’s summarize all the steps you’ve performed (and learned) so far to connect Python with Jira Cloud, fix the empty response issue, and get your board/sprints working.
Here’s your full walkthrough 👇

🧭 1. Set Up Jira Cloud
1. You signed in at https://sab-jan.atlassian.net
2. .
3. Created a Jira Software project (team-managed) — that’s the one showing Summary, Backlog, Board, Timeline, etc.
4. Added a workflow with sprints, and confirmed that the sprint board is visible. ✅ This means the project uses a Scrum template.

🧾 2. Generated a Jira API Token
1. Went to https://id.atlassian.com/manage/api-tokens
2. Clicked “Create API token”
3. Gave it a name (like “Python script”) and copied the token.
4. Saved it securely — Jira tokens are used instead of passwords for REST API access.

🧰 3. Installed Required Library
You used Python’s built-in requests library, so no extra install was required — but if needed, you can always run:


pip install requests

🧩 4. Created the Python Script (jira.py)
Your script connects to Jira’s REST API:


import requests
from requests.auth import HTTPBasicAuth
import json

EMAIL = "your_email@example.com"
API_TOKEN = "your_api_token_here"
url = "https://sab-jan.atlassian.net/rest/api/3/project/search"

auth = HTTPBasicAuth(EMAIL, API_TOKEN)
headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers, auth=auth)

print(response.status_code)
print(json.dumps(response.json(), indent=4))

# replace your email similar to jira account.
# replace apitoken
# replace url add your domain in domain.atlassian.com


🧠 5. Fixed Common Issues
❌ Issue 1: Got an empty response []
✅ Cause: Wrong email / token user didn’t have access to any projects. ✅ Fix:
* Used the same email that logs into Jira Cloud.
* Added that email as a Project Member (via: Project Settings → People → Add people).
* Re-ran the script.

❌ Issue 2: Wrong endpoint
Originally you used:


https://sab-jan.atlassian.net/rest/api/3/project
✅ Correct endpoint to list projects:


https://sab-jan.atlassian.net/rest/api/3/project/search

🧾 6. Verified Output
Once fixed, the correct script prints:


{
  "isLast": true,
  "maxResults": 50,
  "startAt": 0,
  "total": 1,
  "values": [
      {
          "id": "10000",
          "key": "TST",
          "name": "Test Project",
          "projectTypeKey": "software"
      }
  ]
}
This confirms your Python script is now properly connected to Jira via REST API ✅

🧱 7. Verified Jira UI Features
Inside Jira:
* You saw the Board, Backlog, and Sprint views.
* You added a workflow with sprint support, making sprints visible on the board.
* This confirmed the project is set to Scrum mode (not Kanban).

🧩 8. (Optional Next Steps)
Now that it’s working, you can:
Task	Jira API Endpoint	Description
🔹 Create a new issue	/rest/api/3/issue	Add a new task/bug/story
🔹 Create a sprint	/rest/agile/1.0/sprint	Start a new sprint automatically
🔹 Get project details	/rest/api/3/project/{key}	View project info
🔹 Assign users	/rest/api/3/issue/{key}/assignee	Change task owner
🔹 Add comments	/rest/api/3/issue/{key}/comment	Log progress or updates
✅ Final Summary
Step	Action	Result
1️⃣	Created Jira project	“Board”, “Backlog”, “Sprint” visible
2️⃣	Generated API token	Enabled secure API access
3️⃣	Wrote jira.py with requests	Connected Python → Jira
4️⃣	Fixed email and endpoint	Authenticated successfully
5️⃣	Added API user to project	Project became visible via API
6️⃣	Tested with /project/search	Confirmed access (response with project data)


------------------------------

output: to only display name.

import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://sab-jan.atlassian.net/rest/api/3/project/search"

API_TOKEN = "paste your jira Token"

auth = HTTPBasicAuth("sab.jan.02.2001@gmail.com", API_TOKEN)
headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)
name = output["values"][0]["name"]
print(name)


# python3 jira.py
sid
