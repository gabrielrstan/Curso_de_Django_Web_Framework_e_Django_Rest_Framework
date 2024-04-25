-- INSERT INTO user_roles (user_id, role_id)
-- VALUES
-- ()

-- SELECT id,
-- (SELECT id FROM roles r ORDER BY RAND() LIMIT 1) AS qualquer
-- FROM users u; 

INSERT INTO user_roles (user_id, role_id)
SELECT id,
(SELECT id FROM roles r ORDER BY RAND() LIMIT 1) AS qualquer
FROM users u; 