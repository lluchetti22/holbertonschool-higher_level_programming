-- Creates the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switches to the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Creates the table states if it does not exist
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT NBOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);