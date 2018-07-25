
CREATE TABLE cliente (
	nome varchar(255) NOT NULL,
	senha varchar(255) NOT NULL,
	email varchar(255) NOT NULL,
	cpf integer NOT NULL,
	PRIMARY KEY (cpf)
);

CREATE TABLE empresa (
	nome_empresa varchar(255) NOT NULL,
	email_empresa varchar(255) NOT NULL,
	senha_empresa varchar(255) NOT NULL,
	cnpj integer NOT NULL,
	PRIMARY KEY (cnpj)
);

CREATE TABLE estoque (
	cnpj_empresa integer,
	codigo integer NOT NULL,
	nome_produto varchar(255) NOT NULL,
	quantidade integer NOT NULL,
	PRIMARY KEY (codigo),
	FOREIGN KEY (cnpj_empresa) REFERENCES empresa(cnpj)
);


CREATE TABLE compra ( 
	cpf_cliente integer,
	cnpj_empresa integer  NOT NULL,
	codigo_produto integer NOT NULL,
	quantidade integer NOT NULL,
	FOREIGN KEY (cpf_cliente) REFERENCES cliente(cpf)
);
