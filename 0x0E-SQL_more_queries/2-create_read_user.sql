-- Create database hbtn_0d_2 if not exists
-- Grant SELECT privilege on database hbtn_0d_2 to user_0d_2
-- Create MySQL server user user_0d_2 if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'%' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
