-- Create a database named hbtn_0d_usa and a table named states, and add a column id with a primary key and auto-increment, a column name with a VARCHAR(256) NOT NULL.

CREATE database If NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);