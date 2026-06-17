# Task 4: Automatic EBS Snapshot Management

This task implements a Python script to manage AWS EBS snapshots for a specified volume. It deletes snapshots older than 30 days and creates a new snapshot for the hardcoded volume.

## What this solution does

- Creates a Boto3 session using the AWS profile `default`.
- Creates an EC2 client in the `us-east-1` region.
- Retrieves all EBS volumes and filters for a specific hardcoded volume ID.
- Lists snapshots for that volume and deletes snapshots older than 30 days.
- Creates a new snapshot for the specified volume.

## Files

- `main.py` - Python script that manages EBS snapshots and prints status messages.
- `README.md` - Documentation for this task.

## Prerequisites

- Python 3.x
- `boto3` installed
- AWS CLI configured with a `default` profile
- IAM permissions for `ec2:DescribeVolumes`, `ec2:DescribeSnapshots`, `ec2:DeleteSnapshot`, and `ec2:CreateSnapshot`

## Setup

1. Install dependencies:

```bash
pip install boto3
```

2. Configure AWS credentials if not already done:

```bash
aws configure --profile default
```

3. Update `main.py` with your specific EBS volume ID:

```python
volume_id = 'vol-0abcd1234efgh5678'
```

## Usage

Run the script from the `TASK4` directory:

```bash
python main.py
```

The script will:

- retrieve volume information
- find snapshots for the configured volume
- delete snapshots older than 30 days
- create a new snapshot for the volume

## Notes

- The current implementation uses a hardcoded volume ID. Change that value before running it in your environment.
- The script assumes the Lambda handler receives a valid Lambda-style `context` object. For local testing, provide an appropriate context or adjust the snapshot-age check.
- Use caution when deleting snapshots: deleted snapshots cannot be recovered unless you have a backup or other copy.
- This script is configured for the `default` AWS profile and `us-east-1` region.
