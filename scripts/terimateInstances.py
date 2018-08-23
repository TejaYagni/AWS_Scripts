import boto3
from botocore.exceptions import EndpointConnectionError
from botocore.exceptions import ParamValidationError

def getInstanceId(instance_toTerminate):
	for i in instance_details:
		if((i["Instances"][0]["State"]["Name"] == 'running') & (i["Instances"][0]["PublicIpAddress"] == instance_toTerminate)):
			return i["Instances"][0]["InstanceId"]

region = raw_input("Enter the region in which the instance you want to terminate is residing.\n")
try:
	session = boto3.session.Session(region_name=region)
	client = session.client('ec2')
	instance_details = client.describe_instances()['Reservations']
except EndpointConnectionError as e:
	print("You have entered a wrong region")
	exit(1)
	
print("Below are the ipaddress of instances")
for i in instance_details:
	if(i["Instances"][0]["State"]["Name"] == 'running'):
		print(i["Instances"][0]["PublicIpAddress"])

instance_toTerminate = raw_input("Enter the ipaddress of running instance that you want to terminate:\n")
try:
	client.terminate_instances(InstanceIds=[getInstanceId(instance_toTerminate)])
	print("Instance terminated")
except ParamValidationError as p:
	print("Invalid IP address entered.")




#print(client.describe_instances()['Reservations'][0]["Instances"][0]['PublicIpAddress'])
#print(client.describe_instances()['Reservations'][1]["Instances"][0]['PublicIpAddress'])
