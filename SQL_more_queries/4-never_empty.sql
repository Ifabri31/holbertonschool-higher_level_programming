-- Create a table named never_empty with the following columns:

CREATE TABLE IF NOT EXISTS id_not_null (
id INT DEFAULT 1,
name VARCHAR(256)
);