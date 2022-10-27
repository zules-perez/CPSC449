import boto3
from botocore.exceptions import ClientError

# Zulema Perez
# rancid80s@csu.fullerton.edu
# CPSC 449
# Project 5 - NoSQL
# Due: 11/27/2020

def listRepliesTo(recipient, messageID, dynamodb=None):
	if not dynamodb:
		dynamodb = boto3.resource('dynamodb', endpoint_url = 'http://localhost:8000')
	
	table = dynamodb.Table('Messages')
	
	try:
		response = table.get_item( Key={'recipient': recipient, 'messageID': messageID})
	except ClientError as e:
		print(e.response['Error']['Message'])
	else:
		return response['Item']
		
# Passes Key msgID and username.
if __name__ == '__main__':
	
	message = listRepliesTo('Jason', 2004)
	if message:
		print('List Replies To Successful: ')
		pprint(message, sort_dicts=False)
