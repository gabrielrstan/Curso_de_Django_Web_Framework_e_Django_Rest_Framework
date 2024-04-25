SELECT u.id AS uid, p.id AS pid, u.first_name 
FROM users AS u
LEFT JOIN profiles AS p
ON u.id  = p.user_id;
