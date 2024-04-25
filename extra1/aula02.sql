-- 	SELECT  * FROM users u;

-- SELECT  email, id, first_name  FROM users u;

-- SELECT  email as e, id as i, first_name as fn 
-- FROM users as u;

SELECT  u.email as uemail, u.id as uid, u.first_name as ifirst_name 
FROM users as u;