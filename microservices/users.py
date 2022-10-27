# users.py

# CPSC 449-01
# Project 2 - Microservices 
# Zulema Perez 
# rancid80s@csu.fullerton.edu


from flask_api import FlaskAPI, status, exceptions
from flask import Flask, request
from werkzeug.security import generate_password_hash, check_password_hash
from timelines import timelineservice_api
import pugsql
import click

app = FlaskAPI(__name__)
app.config.from_envvar('APP_CONFIG')
app.register_blueprint(timelineservice_api)

dbquery = pugsql.module('dbquery/')
dbquery.connect(app.config['DATABASE_URL'])

# Added Custom command.
# Initializes the database with dbquery and insterted data from schema.sql.
@app.cli.command('init')
def init_db():
	with app.app_context():
		db = dbquery.engine.raw_connection()
		with app.open_resource('schema.sql', mode = 'r') as f:
			db.cursor().executescript(f.read())
		db.commit()

# Returns the User Table.
# Using HTTpie -
# http http://127.0.0.1:<PORT>/users
@app.route('/users', methods = ['GET'])
def allUsers():
	all_users = dbquery.all_users()
	return list(all_users), status.HTTP_200_OK
	
# Creates new user.
# Using HTTpie -
# http POST http://127.0.0.1:<PORT>/users/createuser username='' email='' password=''
@app.route('/users/createuser', methods = ['POST'])
def createUser():
	if not request.json:
		raise exceptions.ParseError('Error, request not found.')
	if not('username' and 'email' and 'password' in request.json):
		raise exceptions.ParseError('Error, missing or incorrect parameters.')
	username = request.json['username']
	email = request.json['email']
	hashedpw = generate_password_hash(request.json['password'], method='pbkdf2:sha256', salt_length = 8)
	try:
		dbquery.create_user(username = username, email = email, hashedpw = hashedpw)
	except Exception as e:
		return {'error': str(e)}, status.HTTP_409_CONFLICT
	return{'success': 'User account created.'}, status.HTTP_200_OK
	
# Authenticates user.
# Using HTTpie -
# http GET http://127.0.0.1:<PORT>/users/authenticate username=='' hashedpw==''
@app.route('/users/authenticate', methods = ['GET'])
def authenticateUser():
	user = dbquery.authenticate_user(username = request.args['username'], hashedpw = request.args['hashedpw'])
	if not list(user):
		return{'error': 'Invalid username or password'}, status.HTTP_403_FORBIDDEN
	return{'success': 'user authenticated.'}, status.HTTP_200_OK

# Populates a list of users a specific user is following
# Using HTTpie -
# http http://127.0.0.1:<PORT>/users/following username==''
@app.route('/users/following', methods = ['GET'])
def allFollowedUsers():
	followed_user = dbquery.check_followingusers(user_following = request.args['username'])
	return list(followed_user), status.HTTP_200_OK

# Starts following a specific new user.
# Using HTTpie -
# http http://127.0.0.1:<PORT>/users/follow followed_user='' user_following=''
@app.route('/users/follow', methods = ['POST'])
def addFollower():
	followed_user = request.json['followed_user']
	user_following = request.json['user_following']
	if not checkforUser(followed_user) or not checkforUser(user_following):
		return{'error': 'Username does not exist.'}, status.HTTP_400_BAD_REQUEST
	try:
		dbquery.startfollowing_user(followed_user = followed_user, user_following = user_following)
	except Exception as e:
		return{'error': str(e)}, status.HTTP_400_CONFLICT
	return{'success': ' ' + user_following + ' is now following ' + followed_user}, status.HTTP_200_OK

# Stops following a specific user.
# Using HTTpie -
# http DELETE http://127.0.0.1:<PORT>/users/unfollow followed_user='' user_following=''
@app.route('/users/unfollow', methods = ['DELETE'])
def removeFollower():
	followed_user = request.json['followed_user']
	user_following = request.json['user_following']
	if not checkifFollowing(followed_user, user_following):
		return{'error': 'Username does not exist or is not following the user.'}, status.HTTP_400_BAD_REQUEST
		
	dbquery.stop_following(followed_user = followed_user, user_following = user_following)
	return {'success': ' ' + user_following + ' is no longer following ' + followed_user}, status.HTTP_200_OK

# Checks if the specific username is stored in the database.
def checkforUser(username):
	check_user = dbquery.check_user(username = username)
	return check_user

# Checks if following a username given a specific user name
def checkifFollowing(followed_user, user_following):
	checkif_following = dbquery.checkif_following(followed_user = followed_user, user_following = user_following)
	return checkif_following
	

