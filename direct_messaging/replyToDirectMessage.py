from pprint import pprint
import boto3
import random

# Zulema Perez
# rancid80s@csu.fullerton.edu
# CPSC 449
# Project 5 - NoSQL
# Due: 11/27/2020

def replyToDirectMessage(messageID, recipient, sender, reply, quickReplies=None, dynamodb=None):
	
	if not dynamodb:
		dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
	
	# Quick reply message options.
	
	if quickReplies == 1:
		reply = 'Can not talk right now.'
	elif quickReplies == 2:
		reply = 'I am on my way!'
	elif quickReplies == 3:
		reply = 'Hi. Hows it going?'
	
	newMessageID = random.randint(0,10000)
	
	table = dynamodb.Table('Messages')
	
	response = table.put_item(
		Item={
			'messageID': newMessageID,
			'recipient': recipient,
			'sender': sender,
			'replyToID': messageID,
			'message': reply,
		}
	)
	return response
	
if __name__== '__main__':
	
	message_response = replyToDirectMessage(1980,"Jason", "Zules", "Test, Testing, Testing 123.", 3)
	print('Reply To Direct Message Successful: ')
	pprint(message_response, sort_dicts=False)
