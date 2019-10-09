-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.9.1-beta
-- PostgreSQL version: 10.0
-- Project Site: pgmodeler.com.br
-- Model Author: ---


-- Database creation must be done outside an multicommand file.
-- These commands were put in this file only for convenience.
-- -- object: new_database | type: DATABASE --
-- -- DROP DATABASE IF EXISTS new_database;
-- CREATE DATABASE new_database
-- ;
-- -- ddl-end --
-- 

-- object: public.filme | type: TABLE --
-- DROP TABLE IF EXISTS public.filme CASCADE;
CREATE TABLE public.filme(
	id serial NOT NULL,
	titulo varchar(150) NOT NULL,
	data_lancamento date NOT NULL,
	CONSTRAINT pk_filme PRIMARY KEY (id)

);
-- ddl-end --
ALTER TABLE public.filme OWNER TO postgres;
-- ddl-end --

-- object: public.ator | type: TABLE --
-- DROP TABLE IF EXISTS public.ator CASCADE;
CREATE TABLE public.ator(
	id serial NOT NULL,
	nome varchar(150) NOT NULL,
	nascimento date NOT NULL,
	CONSTRAINT pk_ator PRIMARY KEY (id)

);
-- ddl-end --
ALTER TABLE public.ator OWNER TO postgres;
-- ddl-end --

-- object: public.filme_ator | type: TABLE --
-- DROP TABLE IF EXISTS public.filme_ator CASCADE;
CREATE TABLE public.filme_ator(
	fk_filme integer NOT NULL,
	fk_ator integer NOT NULL,
	CONSTRAINT pk_filme_ator PRIMARY KEY (fk_filme,fk_ator)

);
-- ddl-end --
ALTER TABLE public.filme_ator OWNER TO postgres;
-- ddl-end --

-- object: public.contato | type: TABLE --
-- DROP TABLE IF EXISTS public.contato CASCADE;
CREATE TABLE public.contato(
	id serial NOT NULL,
	telefone varchar(15) NOT NULL,
	endereco varchar(150) NOT NULL,
	fk_ator integer NOT NULL,
	CONSTRAINT pk_contato PRIMARY KEY (id)

);
-- ddl-end --
ALTER TABLE public.contato OWNER TO postgres;
-- ddl-end --

-- object: public.duble | type: TABLE --
-- DROP TABLE IF EXISTS public.duble CASCADE;
CREATE TABLE public.duble(
	id serial NOT NULL,
	nome varchar(150) NOT NULL,
	ativo bool NOT NULL,
	fk_ator integer NOT NULL,
	CONSTRAINT pk_duble PRIMARY KEY (id)

);
-- ddl-end --
ALTER TABLE public.duble OWNER TO postgres;
-- ddl-end --

-- object: fk_filme | type: CONSTRAINT --
-- ALTER TABLE public.filme_ator DROP CONSTRAINT IF EXISTS fk_filme CASCADE;
ALTER TABLE public.filme_ator ADD CONSTRAINT fk_filme FOREIGN KEY (fk_filme)
REFERENCES public.filme (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_ator | type: CONSTRAINT --
-- ALTER TABLE public.filme_ator DROP CONSTRAINT IF EXISTS fk_ator CASCADE;
ALTER TABLE public.filme_ator ADD CONSTRAINT fk_ator FOREIGN KEY (fk_ator)
REFERENCES public.ator (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_ator | type: CONSTRAINT --
-- ALTER TABLE public.contato DROP CONSTRAINT IF EXISTS fk_ator CASCADE;
ALTER TABLE public.contato ADD CONSTRAINT fk_ator FOREIGN KEY (fk_ator)
REFERENCES public.ator (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: fk_ator | type: CONSTRAINT --
-- ALTER TABLE public.duble DROP CONSTRAINT IF EXISTS fk_ator CASCADE;
ALTER TABLE public.duble ADD CONSTRAINT fk_ator FOREIGN KEY (fk_ator)
REFERENCES public.ator (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --


