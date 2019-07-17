-- Creates the table unique_id on your MySQL server.

CREATE TABLE IF NOT EXISTS id_not_null (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
