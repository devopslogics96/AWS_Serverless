import json

import boto3
def lambda_handler(event, context):
        # Create an S3 client
    aws_console = boto3.session.Session(profile_name='default')
    aws_ec2 = aws_console.client('ec2', region_name='us-east-1')
    # Describe EC2 instances
    response = aws_ec2.describe_instances()
    # Print instance information
    #print(response)
    result=json.dumps(response, indent=4, default=str)
    ressult=response["Reservations"]
    instanceId =  []
    for each in ressult:
        # print("Instance ID:", each["Instances"][0]["InstanceId"])
        # print("Instance Type:", each["Instances"][0]["InstanceType"])
        # print("State:", each["Instances"][0]["State"]["Name"])
        # print("Public IP:", each["Instances"][0].get("PublicIpAddress", "N/A"))
        # print("Launch Time:", each["Instances"][0]["LaunchTime"])
        # print("-" * 40)
        # print("Tags:", each["Instances"][0]["Tags"][0]["Value"])
        instanceId.append([each["Instances"][0]["State"]["Name"],each["Instances"][0]["InstanceId"],each["Instances"][0]["Tags"][0]["Value"] ])
    for each in instanceId:
        if each[0] == "running" and each[2] == 'Auto-Stop':
            aws_ec2.stop_instances(InstanceIds=[each[1]])
            print(f"Stopped instance: {each[1]} with tag: {each[2]}")
        if each[0] == "stopped" and each[2] == 'Auto-Start':
            aws_ec2.start_instances(InstanceIds=[each[1]])
            print(f"Started instance: {each[1]} with tag: {each[2]}")
    return {
        'statusCode': 200,
        'body': json.dumps('EC2 instances have been processed based on their tags.')        
    }
