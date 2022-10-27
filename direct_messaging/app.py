# app.py

# Zulema Perez
# rancid80s@csu.fullerton.edu
# CPSC 449
# Project 5 - NoSQL
# Due: 11/27/2020

import boto3

def create_message_table(dynamodb=None):
	if not dynamodb:
		dynamodb = boto3.resource('dynamodb', endpoint_url = 'http://localhost:8000')
	
	table = dynamodb.create_table(
		TableName='Messages',
		KeySchema=[
			{
				'AttributeName': 'messageID',
				'KeyType': 'HASH'
			},
			{
				'AttributeName': 'recipient',
				'KeyType': 'RANGE'
			},
		],
		AttributeDefinitions=[
			{
				'AttributeName': 'messageID',
				'AttributeType': 'N'
			},
			{
				'AttributeName': 'recipient',
				'AttributeType': 'S'
			},
		],
		ProvisionedThroughput={
			'ReadCapacityUnits': 10,
			'WriteCapacityUnits': 10
		}
	)
	return table

if __name__ == '__main__':

	message_table = create_message_table()
	print('Table Status: ', message_table.table_status)
