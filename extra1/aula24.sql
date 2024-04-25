SELECT first_name, COUNT(id) AS total 
FROM users u
GROUP BY first_name 
ORDER BY total DESC; 

SELECT u.first_name , COUNT(u.id) AS total  FROM users u
JOIN profiles p
ON p.user_id = u.id 
WHERE u.first_name = 'Gabriel'
GROUP BY first_name 
ORDER BY total DESC 
LIMIT 5;