-- Crear base de datos
CREATE DATABASE IF NOT EXISTS crazydb;

-- Usar la base de datos
USE crazydb;

-- Crear la tabla crazyusers
CREATE TABLE IF NOT EXISTS crazyusers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Insertar datos en la tabla crazyusers
INSERT INTO crazyusers (user, password) VALUES ('oneimg', '1000w3rd5');
