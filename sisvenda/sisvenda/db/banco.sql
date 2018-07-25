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



CREATE TABLE "compra" (
	"cpf_cliente" integer(255) NOT NULL,
	"cnpj_empresa" integer(255) NOT NULL,
	"codigo_produto" integer(255) NOT NULL,
	"quantidade" integer(255) NOT NULL
) WITH (
  OIDS=FALSE
);



CREATE TABLE "estoque" (
	"codigo" serial(255) NOT NULL,
	"quantidade" integer(255) NOT NULL,
	CONSTRAINT estoque_pk PRIMARY KEY ("codigo")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "adicionar_produto" (
	"codigo_produto" integer(255) NOT NULL,
	"quantidade_produto" integer(255) NOT NULL,
	"cnpj_empresa" integer(255) NOT NULL
) WITH (
  OIDS=FALSE
);





ALTER TABLE "compra" ADD CONSTRAINT "compra_fk0" FOREIGN KEY ("cpf_cliente") REFERENCES "cliente"("cpf");
ALTER TABLE "compra" ADD CONSTRAINT "compra_fk1" FOREIGN KEY ("cnpj_empresa") REFERENCES "empresa"("cnpj");
ALTER TABLE "compra" ADD CONSTRAINT "compra_fk2" FOREIGN KEY ("codigo_produto") REFERENCES "estoque"("codigo");


ALTER TABLE "adicionar_produto" ADD CONSTRAINT "adicionar_produto_fk0" FOREIGN KEY ("codigo_produto") REFERENCES "estoque"("codigo");
ALTER TABLE "adicionar_produto" ADD CONSTRAINT "adicionar_produto_fk1" FOREIGN KEY ("cnpj_empresa") REFERENCES "empresa"("cnpj");
