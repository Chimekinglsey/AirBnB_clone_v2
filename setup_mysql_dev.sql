-- WE ARE CREATING A DATABSE AND USER WITH SOME PRIVILEGES
-- first we create a database
-- then we create a user identified as hbnb_dev @ localhost
-- we identify the user with a password hbnb_dev_pwd
-- the grant privileges on tables in this database
-- grant select privilege on another database performance_schema
-- I don't see why we have to grant usage Privilege on ALL tables to our user
-- so i ignored this GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost'; though its in
-- the cat file
-- all creation should use IF NOT EXIST to avoid failure on existence

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
