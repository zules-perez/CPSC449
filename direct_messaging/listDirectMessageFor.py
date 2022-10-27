from pprint import pprint
import boto3 
from botocore.exceptions import ClientError

# Zulema Perez
# rancid80s@csu.fullerton.edu
# CPSC 449
# Project 5 - NoSQL
# Due: 11/27/2020

def listDirectMessageFor(recipient, messageID, dynamodb=None):
	if not dynamodb:
		dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
		
	table = dynamodb.Table('Messages')
	
	try:
		response = table.get_item(Key={'recipient': recipient, 'messageID': messageID})
	except ClientError as e:
		print(e.response['Error']['Message'])
	else:
		return response['Item']
		
# Passes the key msgID and username.

if __name__ == '__main__':
	
	message = listDirectMessageFor("Jason", 1980)
	if message:
		print('List Direct Messages For successful: ')
		pprint(message, sort_dicts=False)
