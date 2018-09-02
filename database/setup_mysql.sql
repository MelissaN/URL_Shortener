-- prepares a MySQL server for the project with sample data in database
-- GRANT USAGE ON *.* TO 'root'@'localhost';

CREATE DATABASE IF NOT EXISTS urlshort_dev_db;
-- CREATE USER IF NOT EXISTS urlshort_dev@localhost IDENTIFIED BY '';
USE urlshort_dev_db;
GRANT ALL PRIVILEGES ON urlshort_dev_db TO 'root'@'localhost';
USE performance_schema;
GRANT SELECT ON performance_schema.* TO 'root'@'localhost';
FLUSH PRIVILEGES;

USE urlshort_dev_db;
CREATE TABLE IF NOT EXISTS long_short_urls(
       short_url VARCHAR(255) NOT NULL,
       long_url VARCHAR(255) NOT NULL,
       PRIMARY KEY (short_url)
)
INSERT INTO long_short_urls (short_url, long_url) VALUES ("example", "http://wikipedia.com");
