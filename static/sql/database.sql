# eliminamos la base
DROP DATABASE IF EXISTS Borbocoders;

# creamos la base de datos, con charset UTF8 para que tome correctamente los ascentos
CREATE DATABASE IF NOT EXISTS Borbocoders CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

# usamos la base de datos creada
USE Borbocoders;

DROP TABLE productos;
# creamos a tabla productos
CREATE TABLE productos (
    id TINYINT(255) AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    precio INT(255) NOT NULL,
    imagen VARCHAR(255) NOT NULL
);

# esta entrada nos permite reiniciar la tabla como si nunca se hubieran cargado los productos.
Truncate table productos;

# estos son los productos del JS que tiene los productos
# solamente faltaría ajustar el tema de las rutas de las imágenes una vez que las subamos a algún hosting gratis
INSERT INTO productos (marca, nombre, precio, imagen)
VALUES
('Homen', 'Verum', '45000', '1.jpg'),
('Biografia', 'Assinatura', '36000', '2.jpg'),
('Essencial', 'Clasico', '55000', '3.jpg'),
('Humor', 'Quimica de', '30000', '4.jpg'),
('Kaiak', 'Ultra', '33000', '5.jpg'),
('Kaiak', 'Exclusivo', '55000', '6.jpg'),
('Luna', 'Absoluta', '39000', '7.jpg'),
('Kriska', 'Drama', '26000', '8.jpg'),
('Kriska', 'Alegria', '26000', '9.jpg'),
('Luna', 'Intenso', '42000', '10.jpg'),
('Ekos', 'Alma', '42000', '11.jpg'),
('Essencial', 'Supreme', '39000', '12.jpg')
;