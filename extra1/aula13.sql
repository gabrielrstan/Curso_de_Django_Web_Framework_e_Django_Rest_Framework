SELECT u.id AS uid, p.id AS pid  
FROM users AS u, profiles AS p
WHERE u.id = p.id;