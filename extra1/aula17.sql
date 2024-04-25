-- SELECT ROUND( RAND() * 10000, 2); 

-- UPDATE users SET salary = ROUND( RAND() * 10000, 2); 

SELECT first_name, salary 
FROM users u 
WHERE salary BETWEEN 1000 and 1500
ORDER BY salary ASC;