CREATE TABLE produtos (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    preco DECIMAL(6, 2) NOT NULL,
    descricao VARCHAR(500),
    quantidade INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE clientes (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL,
    fl_ativo BOOL NOT NULL DEFAULT true
);

CREATE TABLE vendas (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	produto_id INTEGER NOT NULL,
    cliente_id INTEGER NOT NULL,
	quantidade INTEGER NOT NULL,
	preco_referencia DECIMAL(6, 2) NOT NULL,
	data_hora DATETIME NOT NULL,
	total DECIMAL(6, 2) NOT NULL,
	FOREIGN KEY (produto_id) REFERENCES produtos(id),
	FOREIGN KEY (cliente_id) REFERENCES clientes(id)
) 