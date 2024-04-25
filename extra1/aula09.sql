-- SELECT id, first_name, email  
-- from users u 
-- WHERE id BETWEEN 50 AND 100
-- ORDER BY id  ASC
-- LIMIT 5 OFFSET 6;

SELECT id, first_name, email  
from users u 
WHERE id BETWEEN 50 AND 100
ORDER BY id  ASC
LIMIT 6,5;