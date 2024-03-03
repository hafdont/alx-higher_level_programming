-- Creates a database hbtn_0d_usa witht the table cities.
-- Grant SELECT privilege on database hbtn_0d_2 to user_0d_2
-- Create MySQL server user user_0d_2 if not exists

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS TABLE 'hbtn_0d_usa'.'cities' (
	PRIMARY KEY('id'),
	'id' INT AUTO_INCREMENT PRIMARY KEY,
	'state_id' INT NOT NULL,
	'name' VARCHAR(256) NOT NULL,
	FOREIN KEY ('state_id')
	REFERENCES 'hbtn_0d_usa'.'states'('id')
);
