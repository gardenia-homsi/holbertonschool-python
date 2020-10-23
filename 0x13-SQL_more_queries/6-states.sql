-- Create database if not exists.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create table in database with constraint.
CREATE TABLE IF NOT EXISTES states.hbtn_0d_usa (
       id INT UNIQUE AUTO_INCREMENT NOT NULL,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY(id)
);
