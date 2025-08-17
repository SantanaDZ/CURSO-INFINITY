CREATE TABLE vendas (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	produto_id INTEGER NOT NULL,
    cliente_id INTEGER NOT NULL,
	quantidade INTEGER NOT NULL,
	preco_referencia DECIMAL(6, 2) NOT NULL,
	data_hora DATETIME NOT NULL,
	total DECIMAL(6, 2) NOT NULL,
	FOREIGN KEY produto_id REFERENCES produtos(id)
	FOREIGN KEY cliente_id REFERENCES clientes(id)
)    