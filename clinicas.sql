-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.9.1
-- PostgreSQL version: 10.0
-- Project Site: pgmodeler.io
-- Model Author: ---


-- Database creation must be done outside a multicommand file.
-- These commands were put in this file only as a convenience.
-- -- object: bd_teste | type: DATABASE --
-- -- DROP DATABASE IF EXISTS bd_teste;
-- CREATE DATABASE bd_teste;
-- -- ddl-end --
-- 

-- object: public.empresas | type: TABLE --
-- DROP TABLE IF EXISTS public.empresas CASCADE;

CREATE TABLE public.ativos(
	id_ativo varchar NOT NULL,
	tipo_ativo char(20),
	descricao_passivo char(20),
	valor_ativo integer,
	data_ativo date,
	CONSTRAINT ativos_pk PRIMARY KEY (id_ativo)

);
-- ddl-end --
ALTER TABLE public.ativos OWNER TO postgres;
-- ddl-end --

-- object: public.passivos | type: TABLE --
-- DROP TABLE IF EXISTS public.passivos CASCADE;
CREATE TABLE public.passivos(
	id_passivo varchar NOT NULL,
	tipo_passivo char(20),
	descricao_passivo char(20),
	valor_passivo integer,
	data_passivo date,
	CONSTRAINT passivos_pk PRIMARY KEY (id_passivo)

);
-- ddl-end --
ALTER TABLE public.passivos OWNER TO postgres;
-- ddl-end --

-- object: public.lucratividade | type: TABLE --
-- DROP TABLE IF EXISTS public.lucratividade CASCADE;

