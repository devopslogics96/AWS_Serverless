import boto3
def main():
    # Create an S3 client
    aws_console = boto3.session.Session(profile_name='default')
    s3_client = aws_console.client(resource_name='s3', region_name='us-east-1')
    # List all buckets    response = s3_client.list_buckets()
    print("Buckets:")
    for bucket in response['Buckets']:
        print(f" - {bucket['Name']}")

if __name__ == "__main__":
    main()