-- 1) Insira 5 usuários

SELECT * FROM users u;
INSERT INTO users (first_name, last_name, email, password_hash, salary) VALUES
("Gabriel", "Stanzione", "gabrielstan@email.com", "gabrielstan", "8000"),
("Roberto", "Stanzione", "robertostanzione@email.com", "roberto", "8000"),
("Alice", "Stanzione", "alicestanzione@email.com", "alice", "8000"),
("Jorge", "Stanzione", "jorgestanzione@email.com", "jorge", "8000"),
("Ruan", "Stanzione", "ruanstanzione@email.com", "ruan", "8000");

-- 2) Insira 5 perfís para os usuários inserido

INSERT INTO profiles (bio, description, user_id)
SELECT CONCAT("Bio de ", u.first_name), CONCAT("Description de ", u.first_name), u.id from  users u 
LEFT JOIN profiles p 
ON p.user_id = u.id  
WHERE u.id BETWEEN 108 AND 112;

-- 3) Insira permissões (roles) para os usuários inseridos

INSERT INTO user_roles (user_id, role_id)
SELECT id,
(SELECT id FROM roles r ORDER BY RAND() LIMIT 1) AS qualquer
FROM users u
WHERE u.id BETWEEN 108 AND 112;

-- 4) Selecione os últimos 5 usuários por ordem decrescente

SELECT * from users u
WHERE u.id BETWEEN 108 AND 112
ORDER BY u.id DESC ;

-- 5) Atualize o último usuário inserido

UPDATE users SET last_name = "Sila" WHERE id = 112;
 
SELECT * FROM users u WHERE u.id = 112

-- 6) Remova uma permissão de algum usuário

DELETE FROM user_roles WHERE user_id = 112 AND role_id = 6;

SELECT * FROM user_roles ur
WHERE user_id = 112

-- 7) Remova um usuário que tem a permissão "PUT"
	
	DELETE FROM users WHERE id = 108;

	SELECT u.first_name, r.name, u.id  from users u 
	INNER JOIN user_roles ur  
	ON u.id = ur.user_id
	INNER JOIN roles r
	ON r.id = ur.role_id 
	ORDER BY u.first_name 

-- 8) Selecione usuários com perfís e permissões (obrigatório)

SELECT first_name, ur.role_id, r.name  FROM users u
INNER JOIN profiles p 
ON p.user_id = u.id 
INNER JOIN user_roles ur 
INNER JOIN roles r 
ON r.id = ur.role_id 
ON u.id = ur.user_id
ORDER BY u.first_name;
	
-- 9) Selecione usuários com perfís e permissões (opcional)

SELECT first_name, ur.role_id, r.name, p.user_id  FROM users u
LEFT JOIN profiles p 
ON p.user_id = u.id 
LEFT JOIN user_roles ur 
LEFT JOIN roles r 
ON r.id = ur.role_id 
ON u.id = ur.user_id
ORDER BY p.user_id

-- 10) Selecione usuários com perfís e permissões ordenando por salário

SELECT first_name, ur.role_id, r.name, u.salary  FROM users u
INNER JOIN profiles p 
ON p.user_id = u.id 
INNER JOIN user_roles ur 
INNER JOIN roles r 
ON r.id = ur.role_id 
ON u.id = ur.user_id
ORDER BY u.salary;
