import boto3
from datetime import datetime, timedelta
import json

aws_console = boto3.session.Session(profile_name='default')
s3_client = aws_console.client('s3', region_name='us-east-1')

def is_s3_object_older_than_one_month(bucket_name, object_key):
    try:
        response = s3_client.head_object(Bucket=bucket_name, Key=object_key)
        last_modified = response['LastModified']
        
        # Remove timezone info for comparison
        last_modified = last_modified.replace(tzinfo=None)
        current_date = datetime.now()
        one_month_ago = current_date - timedelta(days=0)
        
        return last_modified < one_month_ago
    
    except Exception as e:
        print(f"Error: {e}")
        return False

def lambda_handler(event, context):
    # List all buckets    
    response = s3_client.list_buckets()
    print("Buckets:")
    for bucket in response['Buckets']:
        print(f"  - {bucket['Name']}")
        objects = s3_client.list_objects_v2(Bucket=bucket['Name'])
        print("  Objects:")
        for obj in objects.get('Contents', []):
            if is_s3_object_older_than_one_month(bucket['Name'], obj['Key']):
                deleted = s3_client.delete_object(Bucket=bucket['Name'], Key=obj['Key'])
                if deleted:
                    print(f"    Deleted: {obj['Key']} (Last Modified: {obj['LastModified']})")  
                else:
                    print(f"    Failed to delete: {obj['Key']} (Last Modified: {obj['LastModified']})")
            else:
                print(f"    Skipped: {obj['Key']} (Last Modified: {obj['LastModified']})")
    return {
        'statusCode': 200,
        'body': json.dumps('S3 objects older than one month have been processed.')
    }