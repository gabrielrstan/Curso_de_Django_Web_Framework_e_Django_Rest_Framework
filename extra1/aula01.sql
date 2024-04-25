# Para usar uma base especifica
-- use base_de_dados;
# Mostra as tabelas que estao no banco
-- show tables;
# Descreve colunas da tabela
DESCRIBE users;
# Inserir registros
INSERT INTO users (first_name, last_name, email, password_hash) values
-- ("Gabriel", "Stanzione", "gabestan@email.com", "gs"),
-- ("Maria", "Monteiro", "mari@email.com", "mari"),
("Ana", "A", "ana@email.com", "ana"),
("Beatriz", "b", "b@email.com", "bea");