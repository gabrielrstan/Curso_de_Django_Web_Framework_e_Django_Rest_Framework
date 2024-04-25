SELECT id, first_name, email  
from users u 
WHERE id BETWEEN 50 AND 100
ORDER BY created_at ASC;