import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Get all EBS snapshots
    response = ec2.describe_snapshots(OwnerIds=['self'])

    # Get all active EC2 instance IDs
    instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    active_instance_ids = set()

    for reservation in instances_response['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])

    # Iterate through each snapshot and delete if it's not attached to any volume or the volume is not attached to a running instance
    for snapshot in response['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')

        if not volume_id:
            # Delete the snapshot if it's not attached to any volume
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted EBS snapshot {snapshot_id} as it was not attached to any volume.")
        else:
            # Check if the volume still exists
            try:
                volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
                if not volume_response['Volumes'][0]['Attachments']:
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.")
            except ec2.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    # The volume associated with the snapshot is not found (it might have been deleted)
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")
---------------------------------------------

🧠 Line-by-Line Explanation
1. Import boto3

import boto3

    Imports the AWS SDK for Python (boto3).

    boto3 lets your Python code communicate with AWS services like EC2, S3, Lambda, etc.

    In this case, we’ll use it to interact with EC2 snapshots and volumes.

2. Define Lambda entry point

def lambda_handler(event, context):

    Every AWS Lambda function needs a handler — the main function AWS runs.

    AWS passes two parameters:

        event: input data (e.g., from a CloudWatch event or API Gateway)

        context: runtime info (like the function name, memory, and execution time left)

3. Create EC2 client

    ec2 = boto3.client('ec2')

    Creates a client object to talk to the EC2 service.

    You’ll use this ec2 variable to call methods like:

        describe_snapshots()

        describe_instances()

        delete_snapshot()

        describe_volumes()

4. Get all EBS snapshots you own

    response = ec2.describe_snapshots(OwnerIds=['self'])

    Calls EC2’s describe_snapshots API.

    The OwnerIds=['self'] filter means:
    → “Give me all EBS snapshots owned by this AWS account.”

    Stores the full response (which includes a Snapshots list) in response.

5. Get all active (running) EC2 instances

    instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    Lists all EC2 instances in your account.

    The Filters parameter restricts it to instances with state "running".

    Stores the output (a nested structure of Reservations and Instances) in instances_response.

6. Create an empty set for active instance IDs

    active_instance_ids = set()

    Creates an empty Python set to store unique instance IDs (e.g., i-0abc123def456).

    A set automatically avoids duplicates.

7–9. Extract instance IDs

    for reservation in instances_response['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])

    The EC2 describe_instances response is structured like:

    Reservations → Instances → InstanceId

    This double loop digs into that structure.

    For each running instance, it extracts the InstanceId and adds it to the active_instance_ids set.

✅ After this, active_instance_ids contains all currently running instance IDs.
10. Loop through every snapshot

    for snapshot in response['Snapshots']:

    Loops through each snapshot you own (from describe_snapshots).

    Each snapshot is a dictionary containing data like:

    {
      "SnapshotId": "snap-0123456789abcdef0",
      "VolumeId": "vol-0123456789abcdef0",
      "State": "completed",
      "StartTime": "...",
      "Description": "...",
    }

11–12. Extract snapshot details

        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')

    snapshot_id: the unique ID of the snapshot.

    volume_id: the ID of the volume from which the snapshot was taken.

        Uses .get() so it won’t crash if VolumeId is missing (returns None instead).

13. Check if snapshot has a volume

        if not volume_id:

    This means the snapshot is not linked to any EBS volume.

    Sometimes snapshots exist without a volume (e.g., the volume was deleted long ago).

14–16. Delete orphaned snapshots

            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted EBS snapshot {snapshot_id} as it was not attached to any volume.")

    Deletes that snapshot from AWS using its ID.

    Logs a message for visibility in CloudWatch Logs.

⚠️ Once deleted, the snapshot cannot be restored — this is permanent.
17–32. If snapshot does have a volume...

        else:
            # Check if the volume still exists
            try:
                volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
                if not volume_response['Volumes'][0]['Attachments']:
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.")
            except ec2.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    # The volume associated with the snapshot is not found (it might have been deleted)
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")

Let’s unpack this part carefully:
17–18. The else: block

    Executes when the snapshot does have a VolumeId.

19–20. Describe the volume

volume_response = ec2.describe_volumes(VolumeIds=[volume_id])

    Checks if that volume still exists.

    If it does, AWS returns info about it (including attachments).

21–24. If volume exists but not attached

if not volume_response['Volumes'][0]['Attachments']:
    ec2.delete_snapshot(SnapshotId=snapshot_id)
    print(...)

    Attachments is a list of where the volume is mounted (e.g., which EC2 instance).

    If it’s empty ([]), the volume is detached (not in use).

    The script then deletes the snapshot, assuming it’s no longer needed.

25–32. Handle errors (volume not found)

except ec2.exceptions.ClientError as e:
    if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
        ec2.delete_snapshot(SnapshotId=snapshot_id)
        print(...)

    If describe_volumes fails (for example, the volume was deleted),
    AWS throws a ClientError.

    The error code 'InvalidVolume.NotFound' confirms that the volume no longer exists.

    In that case, the script deletes the snapshot since it’s considered “orphaned.”

🧾 Summary of Logic
Step	Action	AWS Resource	Result
1	List all snapshots you own	EBS	Get all snapshot IDs
2	List all running instances	EC2	Get all active instance IDs
3	For each snapshot: check its volume	EBS	Determine if it’s still used
4	If no volume or volume deleted	EBS	Delete the snapshot
5	If volume detached	EBS	Delete the snapshot
6	Log deletions	CloudWatch	Track what happened
🧠 Key Takeaways

    You’re identifying orphaned or unused EBS snapshots and deleting them.

    The script assumes that snapshots not linked to active volumes are safe to delete.

    It’s effective but risky if you have backups you want to keep — so tagging and filtering are important for safety.
