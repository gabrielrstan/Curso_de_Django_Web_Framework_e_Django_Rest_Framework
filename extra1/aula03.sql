-- SELECT * FROM  users u 
-- WHERE id=2;

-- SELECT * FROM  users u 
-- WHERE first_name = 'Gabriel';

-- SELECT * FROM  users u 
-- WHERE id>2;

-- SELECT * FROM  users u 
-- WHERE id>=2;

-- SELECT * FROM  users u 
-- WHERE id<>2;

SELECT * FROM  users u 
WHERE created_at < "2024-04-23 13:51:38"
AND first_name = 'Gabriel';