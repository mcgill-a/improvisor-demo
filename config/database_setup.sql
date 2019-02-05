# Database Setup Commands

CREATE DATABASE IF NOT EXISTS improvisor;
USE improvisor;

CREATE TABLE IF NOT EXISTS Example (
    id int NOT NULL AUTO_INCREMENT,
    data varchar(255),
    PRIMARY KEY (ID)
);

INSERT INTO
    Example(data)
VALUES
    ("This is some data");

INSERT INTO
    Example(data)
VALUES
    ("Another item of data");