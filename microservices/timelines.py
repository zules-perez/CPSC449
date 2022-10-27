# timelines.py

# CPSC 449-01
# Project 2 - Microservices 
# Zulema Perez 
# rancid80s@csu.fullerton.edu

import pugsql
import click
from flask_api import FlaskAPI, exceptions, status
from flask import request, Blueprint
from datetime import datetime

timelineservice_api = Blueprint('timelineservice_api', __name__)

dbquery = pugsql.module('dbquery/')
dbquery.connect('sqlite:///database.db')

# Gets a specific user timeline given a username
# Returns the most recent 25 posts from the specific given user.
# http GET http://127.0.0.1:<PORT>/usertimeline?user=''
@timelineservice_api.route('/usertimeline', methods = ['GET'])
def getUserTimeline():
	user = request.args.get('user')
	if not user:
		raise exceptions.ParseError('Error, missing or incorrect parameters.')
		
	storedindb = dbquery.user_storedindb(username = user)
	if not storedindb:
		return{'error': 'Username does not exist'}, status.HTTP_400_BAD_REQUEST
	posts = dbquery.get_userposts(username = user)
	return list(posts), status.HTTP_200_OK

# Gets public timeline, returns the 25 most recent posts from all users.
# http GET http://127.0.0.1:<PORT>/publictimeline
@timelineservice_api.route('/publictimeline', methods = ['GET'])
def getPublicTimeline():
	posts = dbquery.get_allposts()
	return list (posts), status.HTTP_200_OK

# Gets the home timeline, returns 25 of the most recent posts from all users that a specific user is following.
# http GET http://127.0.0.1:<PORT>/hometimeline?user=''
@timelineservice_api.route('/hometimeline', methods = ['GET'])
def getHomeTimeline():
	user = request.args.get('user')
	if not user:
		raise exceptions.ParseError('Error, missing or incorrect parameters.')
		
	storedindb = dbquery.user_storedindb(username = user)
	if not storedindb:
		return {'error': 'Username does not exist'}, status.HTTP_400_BAD_REQUEST
		
	user_followed = list(dbquery.get_userfollowed(username = user))
	followedbylist = []
	for users in user_followed:
		followedbylist.append(users.get('followed_user'))
	
	posts = dbquery.get_followedposts(followed_user = followedbylist)
	return list(posts), status.HTTP_200_OK

# Posts a tweet for a specific username.
# Writes the post to the database and returns success if the user exists.
# http POST http://127.0.0.1:<PORT>/post/create user='' text=''
@timelineservice_api.route('/post/create', methods = ['POST'])
def postTweet():
	if not request.json:
		raise exceptions.ParseError('Error, request not found.')
	if not('user' and 'text' in request.json):
		raise exceptions.ParseError('Error, missing or incorrect parameters.')
	
	user = request.json['user']
	text = request.json['text']
	
	storedindb = dbquery.user_storedindb(username = user)
	if not storedindb:
		return{'error': 'Username does not exist'}, status.HTTP_400_BAD_REQUEST
	
	dbquery.add_userpost(username = user, post = text, current_timestamp = datetime.now())
	return{'success': 'Tweet posted.'}, status.HTTP_200_OK

	

