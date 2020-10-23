-- Create database if not exists.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Select database to use.
USE hbtn_0d_usa;
-- Create user if not exists.
CREATE TABLE IF NOT EXISTS states(
       id INT UNIQUE AUTO_INCREMENT NOT NULL,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY(id)
);
