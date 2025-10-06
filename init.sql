CREATE TABLE IF NOT EXISTS usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50),
  apellido VARCHAR(50)
);

INSERT INTO usuarios (nombre, apellido) VALUES
('Micaela', 'Ramirez'),
('Jorge', 'Gómez'),
('Lucia', 'Martinez');