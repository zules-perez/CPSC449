

PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS FollowsUsers;
DROP TABLE IF EXISTS Posts;

CREATE TABLE Users(
	username VARCHAR(25) NOT NULL UNIQUE,
	email VARCHAR(50) NOT NULL UNIQUE,
	hashedpw VARCHAR(25) NOT NULL	
);

CREATE TABLE FollowsUsers(
	user_following VARCHAR(25) NOT NULL,
	followed_user VARCHAR(25) NOT NULL,
	FOREIGN KEY(user_following) REFERENCES Users(username)
	FOREIGN KEY(followed_user) REFERENCES Users(username)
);

CREATE TABLE Posts(
	postauthor VARCHAR(25) NOT NULL,
	postbody VARCHAR(275) NOT NULL,
	time_stamp DATETIME NOT NULL,
	FOREIGN KEY(postauthor) REFERENCES Users(username)
);

-- Sample data to test with --

-- User sample data

INSERT INTO Users(username, email, hashedpw) VALUES('rancid', 'rancid@hotmail.com', 'verylongpassword');
INSERT INTO Users(username, email, hashedpw) VALUES('social', 'social@hotmail.com', 'superfunnypassword');
INSERT INTO Users(username, email, hashedpw) VALUES('json', 'json@gmail.com', 'icantthinkofapw');
INSERT INTO Users(username, email, hashedpw) VALUES('spacex','emusk@rocket.com', 'letsallliveonmarsnow');
INSERT INTO Users(username, email, hashedpw) VALUES('fullerton', 'fullerton@fullerton.edu','somanyprojects');
INSERT INTO Users(username, email, hashedpw) VALUES('newton', 'gravity@gmail.com', 'allaboutapples');
INSERT INTO Users(username, email, hashedpw) VALUES('einstein', 'relativity@gmail.com', 'itsallrelative');
INSERT INTO Users(username, email, hashedpw) VALUES('lovelace', 'adalove@gmail.com', 'supercomplicatedpassword');
INSERT INTO Users(username, email, hashedpw) VALUES('tesla', 'sparks@hotmail.com', 'alternatingcurrent');
INSERT INTO Users(username, email, hashedpw) VALUES('curie', 'radioactive@hotmail.com', 'itwasallworthit');
INSERT INTO Users(username, email, hashedpw) VALUES('longbeach', 'longbeach@csulb.edu', 'maybenextmasters');
-- FollowsUser sample data

INSERT INTO FollowsUsers(followed_user, user_following) VALUES('spacex', 'rancid');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('fullerton','rancid');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('einstein','rancid');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('tesla','rancid');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('newton','rancid');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('lovelace','rancid');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('social','rancid');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('json','rancid');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('curie','rancid');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('longbeach','rancid');

INSERT INTO FollowsUsers(followed_user, user_following) VALUES('curie','tesla');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('newton','tesla');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('lovelace','tesla');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('spacex', 'tesla');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('einstein','tesla');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('fullerton','longbeach');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('tesla','newton');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('social','json');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('json','social');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('tesla','curie');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('longbeach','fullerton');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('einstein','newton');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('curie','einstein');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('newton','einstein');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('curie','lovelace');
INSERT INTO FollowsUsers(followed_user, user_following) VALUES('einstein','spacex');


-- Posts sample data

INSERT INTO Posts(postauthor, postbody, time_stamp) VALUES('rancid','Why isnt anyone else posting!','2020-10-01 12:00:00');
INSERT INTO Posts(postauthor, postbody, time_stamp) VALUES('spacex','I am moving to mars at the end of the month. Does anyone have extra boxes? I need to start packing.','2020-10-02 10:35:15');
INSERT INTO Posts(postauthor, postbody, time_stamp) VALUES('newton','I cut down an apple tree today because they kept falling on my head while I was trying to take a nap.','2020-10-03 05:23:03');
INSERT INTO Posts(postauthor, postbody, time_stamp) VALUES('fullerton','Last minute projects are posted today and are due tomorrow. Good luck.','2020-10-04 3:05:10');
INSERT INTO Posts(postauthor, postbody, time_stamp) VALUES('einstein','E = MC Squared. Enough said.','2020-10-03  01:49:57');

COMMIT;
