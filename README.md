# template_py
initial template for bnka backend

--PASOS PARA LEVANTAR LA APP

1- asociar a base de datos de mysql en archivo .env

2- crear en la base de datos tabla product:
    CREATE TABLE product (
        id INT AUTO_INCREMENT PRIMARY KEY,
        body VARCHAR(255) NOT NULL,
        title VARCHAR(255) NOT NULL,
        userId INT NOT NULL
    );

3-ejecutar los comandos ubicados en comandos.txt

4-importar en postman las colecciones de la api para probar:
    API PRODUCTS BD.postman_collection          --rutas para probar la bd
    API PRODUCTS SERVICE.postman_collection     --rutas para probar el service