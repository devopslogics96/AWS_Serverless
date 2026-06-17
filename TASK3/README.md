# Task 3: Monitor S3 Bucket Encryption

This task implements a Python script that lists all S3 buckets for the configured AWS profile and reports each bucket's server-side encryption configuration.

## What this solution does

- Creates a Boto3 session using the AWS profile `default`.
- Lists all S3 buckets in the configured account.
- Calls `get_bucket_encryption()` for each bucket.
- Prints the bucket name and the encryption algorithm returned by the bucket's encryption configuration.

## Files

- `main.py` - Python script that performs the S3 bucket encryption lookup and prints the encryption type for each bucket.
- `README.md` - Documentation for this task.

## Prerequisites

- Python 3.x
- `boto3` installed
- AWS CLI configured with a `default` profile
- IAM permissions for `s3:ListBucket` and `s3:GetBucketEncryption`

## Setup

1. Install dependencies:

```bash
pip install boto3
```

2. Configure AWS credentials if not already done:

```bash
aws configure --profile default
```

## Usage

Run the script from the `TASK3` directory:

```bash
python main.py
```

The script will:

- list all accessible S3 buckets
- retrieve the server-side encryption configuration for each bucket
- print the encryption algorithm for each bucket

## Notes

- Buckets without a server-side encryption configuration may cause `get_bucket_encryption()` to fail with a `ClientError`.
- For a production-ready solution, add exception handling to identify unencrypted buckets separately.
- This script is currently set to use the `default` AWS profile and the `us-east-1` region for the S3 client.
