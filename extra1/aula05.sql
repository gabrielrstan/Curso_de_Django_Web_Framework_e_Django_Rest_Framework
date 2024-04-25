-- SELECT * FROM users
-- WHERE created_at >= "2020-06-12 17:38:52"
-- AND created_at <= "2020-09-04 19:06:55";

SELECT * FROM users
WHERE created_at BETWEEN  "2020-06-12 17:38:52" AND "2020-09-04 19:06:55";