CREATE DATABASE POSTGRES_DB;

CREATE TABLE sentiment_registry (
	input TEXT PRIMARY KEY NOT NULL,
	compound FLOAT NOT NULL,
	sentiment VARCHAR(20) NOT NULL
);