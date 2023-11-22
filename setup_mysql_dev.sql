-- script that prepares a MySQL server 
-- because SQL the best!
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER  IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'hbnb_dev_pwd';
ALTER USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
