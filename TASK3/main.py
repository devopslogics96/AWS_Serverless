import boto3
import json
def lambda_handler(event, context):
    # Create an S3 client
    aws_console = boto3.session.Session(profile_name='default')
    s3_client = aws_console.client('s3', region_name='us-east-1')
    # List all buckets    
    response = s3_client.list_buckets()
    print("Buckets:")
    list=[]
    for bucket in response['Buckets']:
        response = s3_client.get_bucket_encryption(Bucket=bucket['Name'])
        encriptio_type=response['ServerSideEncryptionConfiguration']['Rules'][0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']
        print(f"  - {bucket['Name']} with encryption type: {encriptio_type}")
        #list.append(response)
    #print(list)   
    return {
        'statusCode': 200,
        'body': json.dumps('S3 buckets and their encryption settings have been retrieved.')
    }

lambda_handler({}, {})