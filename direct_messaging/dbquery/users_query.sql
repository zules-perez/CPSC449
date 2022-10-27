-- :name all_users :many
SELECT * FROM Users

-- :name check_user :one
SELECT * FROM Users WHERE username = :username

-- :name authenticate_user :many
SELECT username FROM Users WHERE (username = :username and hashedpw = :hashedpw)

-- :name check_followingusers :many
SELECT followed_user FROM FollowsUsers WHERE user_following = :user_following

-- :name checkif_following :one
SELECT * FROM FollowsUsers WHERE followed_user = :followed_user and user_following = :user_following

-- :name create_user :insert
INSERT INTO Users(username, email, hashedpw) VALUES(:username, :email, :hashedpw)

-- :name startfollowing_user :insert
INSERT INTO FollowsUsers (followed_user, user_following) VALUES (:followed_user, :user_following)

-- :name stop_following
DELETE FROM FollowsUsers WHERE followed_user = :followed_user and user_following = :user_following
