SELECT u.first_name, p.bio FROM users u 
JOIN profiles AS p 
ON u.id = p.user_id
WHERE u.first_name = 'Katelyn';

UPDATE users AS u 
JOIN profiles AS p 
ON u.id = p.user_id
SET p.bio = CONCAT(p.bio, ' atualizado') 
WHERE u.first_name = 'Katelyn';