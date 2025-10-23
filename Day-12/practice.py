


import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
x = response.json()

for i in x:
    print(i["user"]["login"])

🧠 Step-by-step explanation
1️⃣ import requests
* This imports the Requests library, which allows Python to make HTTP requests (like a browser would).
* It’s used to fetch data from the internet, such as APIs or web pages.

2️⃣ response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
* This line sends an HTTP GET request to the GitHub API endpoint for Kubernetes pull requests.
* GitHub’s API responds with JSON data that contains information about all open pull requests (PRs) for that repository.
✅ So response now holds the server’s response, including:
* Status code (response.status_code)
* Headers (response.headers)
* Data (response.text or response.json())

3️⃣ x = response.json()
* The .json() method converts the JSON response from GitHub into a Python object (a list of dictionaries).
For example, one element of that list looks like:


{
  "url": "https://api.github.com/repos/kubernetes/kubernetes/pulls/12345",
  "id": 12345,
  "title": "Fix API bug",
  "user": {
      "login": "developer123",
      "id": 6789,
      ...
  },
  ...
}

4️⃣ for i in x:
* Loops through each pull request in the list.
Each i is a dictionary that represents one pull request.

5️⃣ print(i["user"]["login"])
* From each PR dictionary (i), you access the "user" key — which is another dictionary — and then get the "login" field from it.
* "login" is the GitHub username of the person who opened that pull request.
✅ So this prints all GitHub usernames who currently have open PRs in the Kubernetes repo.

🧾 Example output
If you ran this successfully, you’d see something like:


alice
bob-dev
charlie99
devopsguru
Each name corresponds to a contributor with an open pull request.

⚡ Optional improvements
1. Check the response status first  

if response.status_code == 200:
    x = response.json()
    for i in x:
        print(i["user"]["login"])
else:
    print("Failed to fetch data:", response.status_code)
Limit how many results you show

1. for i in x[:5]:
2.     print(i["user"]["login"])


Handle rate limits
    * GitHub limits anonymous API requests (about 60 per hour).
    * If you see "API rate limit exceeded", you may need to add authentication.

✅ In summary
Step	Line of code	What it does
1	import requests	Load HTTP library
2	requests.get(...)	Call GitHub API
3	.json()	Convert JSON → Python list
4	for i in x:	Loop through each PR
5	i["user"]["login"]	Print username of each contributor
------------------
for i in range(len(x)):
    print(x[i]["user"]["login"])

🧠 Step-by-Step Explanation
1️⃣ len(x)
* x is the JSON data you got from the GitHub API (a list of pull requests).
* len(x) gives you the number of pull requests in that list. Example: if there are 30 open PRs, len(x) → 30.

2️⃣ range(len(x))
* This creates a sequence of numbers from 0 up to len(x) - 1. Example: range(30) → [0, 1, 2, …, 29]
* These numbers represent the indexes of items in your list x.

3️⃣ for i in range(len(x))
* The loop runs once for each index in x.
    * On the first loop, i = 0
    * On the second loop, i = 1
    * and so on…

4️⃣ x[i]["user"]["login"]
* x[i] gives you the i-th pull request dictionary.
* "user" gives you the nested dictionary with user info.
* "login" gives you the username of the person who opened that pull request.
So for each i, this line prints that username.

🧾 Example Visualization
If x looked like this:

[
  {"user": {"login": "alice"}},
  {"user": {"login": "bob"}},
  {"user": {"login": "charlie"}}
]

len(x) → 3
range(len(x)) → [0, 1, 2]


i	x[i]	x[i]["user"]["login"]	Printed
0	{"user": {"login": "alice"}}	"alice"	alice
1	{"user": {"login": "bob"}}	"bob"	bob
2	{"user": {"login": "charlie"}}	"charlie"	charlie
✅ Output

alice
bob
charlie

for item in x:
    print(item["user"]["login"])

