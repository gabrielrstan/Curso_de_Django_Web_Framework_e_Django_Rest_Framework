SELECT u.first_name, p.bio FROM users u 
LEFT JOIN profiles AS p 
ON u.id = p.user_id
WHERE u.first_name = 'Katelyn';

DELETE p FROM users u 
JOIN profiles AS p 
ON u.id = p.user_id
WHERE u.first_name = 'Katelyn';