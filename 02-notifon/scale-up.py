# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
as_client = session.client('autoscaling')

as_client.execute_policy(AutoScalingGroupName='Notifon Example', PolicyName='Scale Up')

# to scale down auto-scaling group
import boto3
session = boto3.Session(profile_name='pythonAutomation')
as_client = session.client('autoscaling')

as_client.execute_policy(AutoScalingGroupName='Notifon Example', PolicyName='Scale Down')
