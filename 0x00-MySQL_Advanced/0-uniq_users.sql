-- sql script that creates a table user

-- drop table if exist
DROP TABLE IF EXISTS users;

-- create table
CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);
