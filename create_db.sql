BEGIN;
SET client_encoding = 'LATIN1';

CREATE SCHEMA IF NOT EXISTS carford;

-- Creating enums
-- DROP TYPE carford."enumcolor";

CREATE TYPE carford."enumcolor" AS ENUM (
	'yellow',
	'blue',
	'gray');

-- DROP TYPE carford."enummodel";

CREATE TYPE carford."enummodel" AS ENUM (
	'hatch',
	'sedan',
	'convertible');


-- carford.customer definition

-- Drop table

-- DROP TABLE carford.customer;

CREATE TABLE carford.customer (
	id serial4 NOT NULL,
	name varchar NULL,
	email varchar NULL,
	cellphone varchar NULL,
	car_amount int4 NULL,
	CONSTRAINT customer_pkey PRIMARY KEY (id)
);



-- carford.car definition

-- Drop table

-- DROP TABLE carford.car;

CREATE TABLE carford.car (
	id serial4 NOT NULL,
	id_owner int4 NULL,
	model carford.enummodel NULL,
	color carford.enumcolor NULL,
	CONSTRAINT car_pkey PRIMARY KEY (id),
	CONSTRAINT car_id_owner_fkey FOREIGN KEY (id_owner) REFERENCES carford.customer(id)
);

COMMIT;