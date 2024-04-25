SELECT u.id AS uid, p.id AS pid, u.first_name 
FROM users AS u
INNER JOIN profiles AS p
ON u.id  = p.user_id 
WHERE u.first_name LIKE '%a'
ORDER BY u.first_name ASC ;