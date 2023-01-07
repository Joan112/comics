########## DEPENDENCIAS ##########


Para instalar las dependencias necesarias para el proyecto, primero debes asegurarte de tener pip, el administrador de paquetes de Python, instalado en tu sistema. Si no tienes pip instalado, puedes hacerlo ejecutando el siguiente comando en tu terminal:

python -m ensurepip –upgrade

Una vez que tengas pip instalado, puedes utilizar el siguiente comando para instalar las dependencias necesarias a partir del archivo requirements.txt:

pip install -r requirements.txt

Este comando leerá el archivo requirements.txt y instalará cada uno de los paquetes mencionados en el archivo.

Si no tienes el archivo requirements.txt, puedes crearlo manualmente o generarlo automáticamente utilizando el siguiente comando:

pip freeze > requirements.txt

Este comando generará un archivo requirements.txt que contenga todos los paquetes de Python instalados en tu sistema. Puedes usar este archivo para instalar las mismas dependencias en otro sistema.

##################################
consumos postman 
CA2: En caso de no recibir un término de búsqueda, los usuario podrán
acceder los personajes de la A a la Z y navegar por ellos.

http://localhost:5000/searchComics/

CA1: Los usuarios tendrán la posibilidad de realizar una búsqueda por medio
de una palabra (personajes y comics).

http://localhost:5000/searchComics/hulk

CA3: Los usuarios tendrán la posibilidad de agregar un filtro en caso de
querer buscar específicamente un personaje o un comic.

http://localhost:5000/searchComics/hulk/comics


registrar un usuario
http://localhost:5000/register

En la pestaña "Body", selecciona el tipo de cuerpo "raw" y elige el formato "JSON (application/json)" en el menú desplegable.

{
"username": "mi_nombre_de_usuario",
"password": "mi_contraseña"
}

token
http://localhost:5000/user/auth

{
  "username": "gigi",
  "password": "123"
}

##################################