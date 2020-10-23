-- Create database if not exists.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create user if not exists.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Privileges of select in a database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
