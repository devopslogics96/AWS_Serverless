# Task 2: S3 Object Age Check and Cleanup

This task contains a Python script that connects to AWS S3, inspects objects in each bucket, and deletes objects older than one month.

## Files

- `main.py` - AWS Lambda-style script that lists S3 buckets, checks object age, and deletes objects older than one month.

## Prerequisites

- Python 3.x
- `boto3` installed
- AWS CLI configured with a profile named `default` or update the script to use a different profile

## Setup

1. Install dependencies:

```bash
pip install boto3
```

2. Configure AWS credentials:

```bash
aws configure --profile default
```

3. Verify access to S3 via AWS CLI before running the script:

```bash
aws s3 ls --profile default
```

## Usage

Run the script from the `TASK2` directory:

```bash
python main.py
```

The script will:

- list all S3 buckets available to the configured AWS profile
- inspect each object in every bucket
- delete objects whose `LastModified` date is older than one month
- print the deletion or skip status for each object

## Important Notes

- The script currently uses `profile_name='default'` and `region_name='us-east-1'`.
- Be careful with deletion logic: deleted S3 objects cannot be recovered unless versioning or backups are enabled.
- If you want to run this in AWS Lambda, ensure the Lambda execution role has `s3:ListBucket`, `s3:GetObject`, and `s3:DeleteObject` permissions.

## AWS Lambda Deployment

To deploy this code as an AWS Lambda function:

1. Create a Lambda function in the AWS Console or via CLI.
2. Upload the `main.py` file and any required dependencies in a deployment package or use a Lambda layer for `boto3` if needed.
3. Set the handler to `main.lambda_handler`.
4. Choose the Python runtime that matches your environment, such as `Python 3.11`.

### IAM Role Requirements

Create or attach an IAM role with these minimum permissions for the Lambda execution role:

- `s3:ListBucket`
- `s3:GetObject`
- `s3:DeleteObject`

Example IAM policy JSON:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:DeleteObject"
      ],
      "Resource": "arn:aws:s3:::*/*"
    }
  ]
}
```

- Attach this role to your Lambda function before deployment.
- If using one bucket only, scope the `Resource` fields to that bucket and its objects instead of `arn:aws:s3:::*`.

## Customization

- To change the AWS profile, update `profile_name='default'` in `main.py`.
- To target a specific bucket only, modify the bucket iteration logic in `lambda_handler`.
- To change the age threshold, update the `timedelta(days=30)` value in the age-check function.
