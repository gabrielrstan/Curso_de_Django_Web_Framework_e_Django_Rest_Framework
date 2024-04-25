SELECT u.id AS uid, u.first_name, p.bio, r.name AS role_name 
FROM users as u
LEFT JOIN profiles AS p ON u.id = p.user_id 
INNER JOIN user_roles AS ur ON u.id = ur.user_id
INNER JOIN roles AS r ON ur.role_id = r.id 
WHERE u.id = 56
ORDER BY uid ASC ;
