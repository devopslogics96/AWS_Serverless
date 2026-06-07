# Task 1 - EC2 Auto Start/Stop Lambda

This task implements an AWS automation script that inspects EC2 instances in the `us-east-1` region and manages their state based on custom tags.

## What this solution does

- Stops EC2 instances that are in the `running` state and have a tag value of `Auto-Stop`.
- Starts EC2 instances that are in the `stopped` state and have a tag value of `Auto-Start`.

The script is written for both local execution and AWS Lambda deployment.

## Files

- `main.py` - Python script containing:
  - `main()` for local execution
  - `lambda_handler(event, context)` for AWS Lambda
- `README.md` - Usage instructions and implementation details

## Requirements

- Python 3.x installed
- AWS CLI configured with a valid `default` profile
- `boto3` Python library installed
- IAM permissions to call `ec2:DescribeInstances`, `ec2:StopInstances`, and `ec2:StartInstances`

## Setup

1. Install Python dependencies:

```bash
pip install boto3
```

2. Configure AWS credentials if not already configured:

```bash
aws configure --profile default
```

3. Confirm your AWS region and credentials are correct for `us-east-1`.

## How the script works

1. Creates a Boto3 session using the `default` AWS profile.
2. Creates an EC2 client for the `us-east-1` region.
3. Calls `describe_instances()` to retrieve all instances.
4. Iterates through each reservation and instance.
5. Reads the instance state and first tag value.
6. If the state is `running` and tag value is `Auto-Stop`, it stops the instance.
7. If the state is `stopped` and tag value is `Auto-Start`, it starts the instance.
8. Prints a confirmation message for each state change.

## Local execution

Run the script directly from your local environment:

```bash
python main.py
```

This executes the same logic as the Lambda handler and prints which instances were started or stopped.

## Deployment to AWS Lambda

1. Create a deployment package containing `main.py`.
2. Create or choose a Lambda function in AWS.
3. Set the handler to:

```text
main.lambda_handler
```

4. Attach an IAM role to the Lambda function with permissions for EC2 instance describe, stop, and start operations.

## Testing the Lambda function

- Use a scheduled trigger (AWS CloudWatch Events / EventBridge) to run the Lambda periodically.
- You can also invoke the Lambda manually from the AWS Console or using AWS CLI.

### Example AWS CLI invoke

```bash
aws lambda invoke --function-name YourFunctionName output.json
```

## Notes

- The script currently assumes each instance has at least one tag and uses the first tag value.
- If you need support for multiple tags or tag keys, update the tag parsing logic in `main.py`.
- For production use, ensure the Lambda role follows the principle of least privilege.
