-- Create the database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user if it does not already exist and set the password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant only SELECT privilege on the specific database to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to ensure that the changes take effect immediately
FLUSH PRIVILEGES;
