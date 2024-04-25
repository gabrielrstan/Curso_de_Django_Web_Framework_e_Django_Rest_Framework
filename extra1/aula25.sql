SELECT 
	MAX(salary) AS max_salary,
	MIN(salary) AS min_salary,
	AVG(salary) AS avg_salary,
	SUM(salary) AS sum_salary,
	COUNT(salary) AS count_salary 
FROM users u
-- WHERE first_name = 'GABRIEL';

SELECT
	u.first_name ,
	MAX(u.salary) AS max_salary,
	MIN(u.salary) AS min_salary,
	AVG(u.salary) AS avg_salary,
	SUM(u.salary) AS sum_salary,
	COUNT(salary) AS count_salary 
FROM users u
GROUP BY u.first_name ;
