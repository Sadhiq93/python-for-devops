boto3 is used for importing cloud services and maily for serverless services like lamda.
for information to write code of boto3 use documentation as reference.

https://boto3.amazonaws.com/v1/documentation/

Example: to know information of ec2 instance

import boto3
import json

#available in documentation

client = boto3.client('ec2', region_name='ap-south-1') 

response = client.describe_instance_status(
    InstanceIds=['i-06c33f206cd9ee1a7'],
    IncludeAllInstances=True
)

# Pretty-print the response as formatted JSON
print(json.dumps(response, indent=4, sort_keys=True))

✅ Output example:

{
    "InstanceStatuses": [
        {
            "AvailabilityZone": "ap-south-1b",
            "AvailabilityZoneId": "aps1-az3",
            "InstanceId": "i-06c33f206cd9ee1a7",
            "InstanceState": {
                "Code": 80,
                "Name": "stopped"
            },
            "InstanceStatus": {
                "Status": "not-applicable"
            },
            "Operator": {
                "Managed": false
            },
            "SystemStatus": {
                "Status": "not-applicable"
            }
        }
    ],
    "ResponseMetadata": {
        "HTTPHeaders": {
            "cache-control": "no-cache, no-store",
            "content-length": "640",
            "content-type": "text/xml;charset=UTF-8",
            "date": "Mon, 27 Oct 2025 14:19:11 GMT",
            "server": "AmazonEC2",
            "strict-transport-security": "max-age=31536000; includeSubDomains",
            "x-amzn-requestid": "fc565970-4c9f-4752-9163-a85868161ab5"
        },
        "HTTPStatusCode": 200,
        "RequestId": "fc565970-4c9f-4752-9163-a85868161ab5",
        "RetryAttempts": 0
    }
}

If you want only specific parts (like just the instance info), use:

print(json.dumps(response['InstanceStatuses'][0], indent=4, sort_keys=True))

--------------------------------------------------------

🧩 Option 1: Using tabulate (recommended)

Install the package first:

pip install tabulate

Then use this script:

import boto3
from tabulate import tabulate

client = boto3.client('ec2', region_name='ap-south-1')

response = client.describe_instance_status(
    InstanceIds=['i-06c33f206cd9ee1a7'],
    IncludeAllInstances=True
)

# Collect table data
table = []
for instance in response['InstanceStatuses']:
    table.append([
        instance['InstanceId'],
        instance['InstanceState']['Name'],
        instance['AvailabilityZone'],
        instance['SystemStatus']['Status'],
        instance['InstanceStatus']['Status']
    ])

# Define headers
headers = ["Instance ID", "State", "AZ", "System Status", "Instance Status"]

# Print table
print(tabulate(table, headers=headers, tablefmt="grid"))

✅ Example output:

+-----------------------+----------+--------------+------------------+------------------+
| Instance ID           | State    | AZ           | System Status    | Instance Status  |
+-----------------------+----------+--------------+------------------+------------------+
| i-06c33f206cd9ee1a7   | stopped  | ap-south-1b  | not-applicable   | not-applicable   |
+-----------------------+----------+--------------+------------------+------------------+

🧱 Option 2: Without any external library (just f-strings)

import boto3

client = boto3.client('ec2', region_name='ap-south-1')

response = client.describe_instance_status(
    InstanceIds=['i-06c33f206cd9ee1a7'],
    IncludeAllInstances=True
)

print(f"{'Instance ID':<20} {'State':<10} {'AZ':<15} {'System Status':<20} {'Instance Status':<20}")
print("-" * 85)

for instance in response['InstanceStatuses']:
    print(f"{instance['InstanceId']:<20} "
          f"{instance['InstanceState']['Name']:<10} "
          f"{instance['AvailabilityZone']:<15} "
          f"{instance['SystemStatus']['Status']:<20} "
          f"{instance['InstanceStatus']['Status']:<20}")

✅ Example output:

Instance ID          State      AZ              System Status        Instance Status
-------------------------------------------------------------------------------------
i-06c33f206cd9ee1a7  stopped    ap-south-1b     not-applicable       not-applicable


------------
🧩 1. The <20, <10, etc.

These come from formatted string literals (f-strings) in Python — they control how wide each column is when you print text.

Example:
print(f"{'Instance ID':<20} {'State':<10}")

:<20 → means left-align the text in a space 20 characters wide

:<10 → means left-align the text in a space 10 characters wide

So each column will always take up a fixed width, making the text line up neatly like a table.

If your data is shorter than the width, spaces are added to the right to fill it.

----------

🧱 2. The "-" * 85

That’s a simple way to print a horizontal line across the terminal.

"–" is a string with one dash

* 85 repeats it 85 times

