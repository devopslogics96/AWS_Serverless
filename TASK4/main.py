import boto3
import json

def lambda_handler(event, context):
    #create an ebs client
    aws_console = boto3.session.Session(profile_name='default')
    ebs_client = aws_console.client('ec2', region_name='us-east-1')
    #list all volumes
    response = ebs_client.describe_volumes()
    #Check all snapshots older than 30 days and delete them
    for volume in response['Volumes']:
        for snapshot in volume['Snapshots']:
            snapshot_id = snapshot['SnapshotId']
            snapshot_date = snapshot['StartTime']
            if (datetime.now() - snapshot_date).days > 30:
                ebs_client.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Deleted snapshot {snapshot_id} from volume {volume['VolumeId']}")
