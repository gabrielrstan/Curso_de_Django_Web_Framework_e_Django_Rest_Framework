SELECT u.id AS uid, p.id AS pid, u.first_name 
FROM users AS u
RIGHT JOIN profiles AS p
ON u.id  = p.user_id;