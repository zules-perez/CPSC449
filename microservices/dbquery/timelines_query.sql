-- :name user_storedindb :one
SELECT * FROM Users WHERE username = :username

-- :name get_userposts :many
SELECT * FROM Posts WHERE postauthor LIKE (:username) ORDER BY time_stamp DESC LIMIT 25

-- :name get_userfollowed :many
SELECT * FROM FollowsUsers where user_following LIKE (:username)

-- :name get_followedposts :many
SELECT * FROM Posts WHERE postauthor IN :followed_user ORDER BY time_stamp DESC LIMIT 25

-- :name get_allposts :many
SELECT * FROM Posts ORDER BY time_stamp DESC LIMIT 25

-- :name add_userpost :insert
INSERT INTO Posts VALUES (:username, :post, :current_timestamp) 

