-- Create a Database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a User with localhost
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd'

-- Grant Usage
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost'

-- Grant SELECT privilege on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Grant all privileges on the hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
