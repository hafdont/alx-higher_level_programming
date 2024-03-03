-- Creates a database hbtn_0d_usa witht the table cities.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS TABLE cities (
	PRIMARY KEY('id'),
	'id' INT AUTO_INCREMENT PRIMARY KEY,
	'state_id' INT NOT NULL,
	'name' VARCHAR(256) NOT NULL,
	FOREIN KEY ('state_id')
	REFERENCES 'hbtn_0d_usa'.'states'('id')
);
