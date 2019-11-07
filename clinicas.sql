-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.9.1
-- PostgreSQL version: 10.0
-- Project Site: pgmodeler.io
-- Model Author: ---


-- Database creation must be done outside a multicommand file.
-- These commands were put in this file only as a convenience.
-- -- object: new_database | type: DATABASE --
-- -- DROP DATABASE IF EXISTS new_database;
-- CREATE DATABASE new_database;
-- -- ddl-end --
-- 

-- object: public.empresas | type: TABLE --
-- DROP TABLE IF EXISTS public.empresas CASCADE;
CREATE TABLE public.empresas(
	id_cliente smallint NOT NULL,
	"nome fantasia" varchar(50),
	"nome juridico" varchar(50),
	cnpj varchar(11) NOT NULL,
	CONSTRAINT clientes_pk PRIMARY KEY (id_cliente)

);
-- ddl-end --
ALTER TABLE public.empresas OWNER TO postgres;
-- ddl-end --

-- object: public.contatos | type: TABLE --
-- DROP TABLE IF EXISTS public.contatos CASCADE;
CREATE TABLE public.contatos(
	nome char(50),
	sobrenome char(50),
	telefone varchar,
	celular varchar(10),
	id_cliente_empresas smallint
);
-- ddl-end --
ALTER TABLE public.contatos OWNER TO postgres;
-- ddl-end --

-- object: empresas_fk | type: CONSTRAINT --
-- ALTER TABLE public.contatos DROP CONSTRAINT IF EXISTS empresas_fk CASCADE;
ALTER TABLE public.contatos ADD CONSTRAINT empresas_fk FOREIGN KEY (id_cliente_empresas)
REFERENCES public.empresas (id_cliente) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: contatos_uq | type: CONSTRAINT --
-- ALTER TABLE public.contatos DROP CONSTRAINT IF EXISTS contatos_uq CASCADE;
ALTER TABLE public.contatos ADD CONSTRAINT contatos_uq UNIQUE (id_cliente_empresas);
-- ddl-end --

-- object: public.funcionarios | type: TABLE --
-- DROP TABLE IF EXISTS public.funcionarios CASCADE;
CREATE TABLE public.funcionarios(
	id_func smallint NOT NULL,
	nome smallint,
	nr_func smallint,
	CONSTRAINT funcionarios_pk PRIMARY KEY (id_func)

);
-- ddl-end --
ALTER TABLE public.funcionarios OWNER TO postgres;
-- ddl-end --

-- object: public.ativos | type: TABLE --
-- DROP TABLE IF EXISTS public.ativos CASCADE;
CREATE TABLE public.ativos(
	id_ativo smallint,
	nome smallint,
	valor smallint
);
-- ddl-end --
ALTER TABLE public.ativos OWNER TO postgres;
-- ddl-end --

-- object: public.passivos | type: TABLE --
-- DROP TABLE IF EXISTS public.passivos CASCADE;
CREATE TABLE public.passivos(
	id_passivo smallint NOT NULL,
	nome smallint,
	CONSTRAINT passivos_pk PRIMARY KEY (id_passivo)

);
-- ddl-end --
ALTER TABLE public.passivos OWNER TO postgres;
-- ddl-end --

-- object: public.lucratividade | type: TABLE --
-- DROP TABLE IF EXISTS public.lucratividade CASCADE;
CREATE TABLE public.lucratividade(
	id smallint NOT NULL,
	lucro_liquido_anual smallint,
	receita_total_anual smallint,
	CONSTRAINT lucratividade_pk PRIMARY KEY (id)

);
-- ddl-end --
ALTER TABLE public.lucratividade OWNER TO postgres;
-- ddl-end --

-- object: public.turnover | type: TABLE --
-- DROP TABLE IF EXISTS public.turnover CASCADE;
CREATE TABLE public.turnover(
	id smallint,
	contratados smallint,
	desligamentos smallint,
	id_func_funcionarios smallint
);
-- ddl-end --
ALTER TABLE public.turnover OWNER TO postgres;
-- ddl-end --

-- object: public.ticket_medio_vendas | type: TABLE --
-- DROP TABLE IF EXISTS public.ticket_medio_vendas CASCADE;
CREATE TABLE public.ticket_medio_vendas(
	id smallint,
	total_receita smallint,
	total_vendas smallint,
	nr_compras smallint,
	periodo date
);
-- ddl-end --
ALTER TABLE public.ticket_medio_vendas OWNER TO postgres;
-- ddl-end --

-- object: public.taxa_conversao | type: TABLE --
-- DROP TABLE IF EXISTS public.taxa_conversao CASCADE;
CREATE TABLE public.taxa_conversao(
	visitantes smallint,
	id smallint,
	conversoes smallint
);
-- ddl-end --
ALTER TABLE public.taxa_conversao OWNER TO postgres;
-- ddl-end --

-- object: public.roi | type: TABLE --
-- DROP TABLE IF EXISTS public.roi CASCADE;
CREATE TABLE public.roi(
	id smallint,
	receita smallint,
	custo smallint,
	item smallint
);
-- ddl-end --
ALTER TABLE public.roi OWNER TO postgres;
-- ddl-end --

-- object: public.indicadores_negativos | type: TABLE --
-- DROP TABLE IF EXISTS public.indicadores_negativos CASCADE;
CREATE TABLE public.indicadores_negativos(
	id smallint,
	questao smallint
);
-- ddl-end --
ALTER TABLE public.indicadores_negativos OWNER TO postgres;
-- ddl-end --

-- object: funcionarios_fk | type: CONSTRAINT --
-- ALTER TABLE public.turnover DROP CONSTRAINT IF EXISTS funcionarios_fk CASCADE;
ALTER TABLE public.turnover ADD CONSTRAINT funcionarios_fk FOREIGN KEY (id_func_funcionarios)
REFERENCES public.funcionarios (id_func) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: turnover_uq | type: CONSTRAINT --
-- ALTER TABLE public.turnover DROP CONSTRAINT IF EXISTS turnover_uq CASCADE;
ALTER TABLE public.turnover ADD CONSTRAINT turnover_uq UNIQUE (id_func_funcionarios);
-- ddl-end --


