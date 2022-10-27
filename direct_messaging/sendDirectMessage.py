from pprint import pprint
import boto3
import random

# Zulema Perez
# rancid80s@csu.fullerton.edu
# CPSC 449
# Project 5 - NoSQL
# Due: 11/27/2020

def sendDirectMessage(recipient, sender, message, quickReplies=None, dynamodb=None):
	
	if not dynamodb:
		dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
		
	# Quick reply message options.
	
	if quickReplies == 1:
		message = 'Can not talk right now.'
	elif quickReplies == 2:
		message = 'I am on my way.'
	elif quickReplies == 3:
		message = 'Hi. Hows it going?'
	
	messageID = random.randint(0,10000)
	
	table = dynamodb.Table('Messages')
	response = table.put_item(
		Item={
			'messageID': messageID,
			'recipient': recipient,
			'sender': sender,
			'message': message,
		}
	)
	return response
	
if __name__ == '__main__':
	message_response = sendDirectMessage("Zules", "Jason", "Test, Testing, Testing 123.", 1)
	print('Send Direct Message Successful: ')
	pprint(message_response, sort_dicts=False)
