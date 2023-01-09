import json
from urllib import response
from flask import Flask, abort, jsonify, request
import jwt
import public.Functions as Functions
import database.con_bd


app = Flask(__name__)
app.config["SECRET_KEY"] = "mi_clave_secreta"


@app.route("/searchComics/")
def get_All():
    respuesta_get_all = Functions.get_all_personaje()
    respuesta_get_all_comics = Functions.get_all_comics()
    return respuesta_get_all + respuesta_get_all_comics


@app.route("/searchComics/<keyword>")
def search(keyword):
    respuesta = Functions.characters(keyword)
    respuesta2 = Functions.comics(keyword)
    return respuesta + respuesta2


@app.route("/searchComics/<keyword>/<keyword2>")
def search2(keyword, keyword2):
    if keyword2 == 'comics':
        respuesta2 = Functions.comics(keyword)
        return respuesta2
    elif keyword2 == 'personaje':
        respuesta = Functions.characters(keyword)
        return respuesta


@app.route("/user/register/", methods=["POST"])
def register():
    # obtener el cuerpo de una solicitud HTTP
    data = request.get_json()
    return Functions.register_user(data)

# Implementar la ruta de autenticación


@app.route("/user/auth", methods=["POST"])
def authenticate_user():
    # Recibir y validar las credenciales del usuario
    data = request.get_json()
    responce = Functions.auth(data)
    return responce


@app.route("/user/<username>")
def search3(username):
    respuesta = Functions.logged(username)
    return respuesta


@app.route('/addToLayaway', methods=['POST'])
def add_comic():
    # obtener el token del encabezado de autorización
    auth_header = request.headers.get('Authorization')
    if auth_header:
        # verificar que el token sea válido y obtener el nombre de usuario del payload
        try:
            token = auth_header.split(' ')[1]
            # print(token)
            payload = jwt.decode(token, app.config["SECRET_KEY"], algorithms='HS256')
            # print(payload)
            username = payload['username']
            # print(username)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return 'Token inválido', 401

        # obtener los datos del cómic de la solicitud
        data = request.get_json()
        personaje = data["personaje"]
        respuesta = Functions.characters(personaje)
        print( respuesta)
        if respuesta[1] == 400:

            return jsonify("El personaje no se encuentra en la Api de marvel")
        #     print("aqui")
        #     return abort(400, "Error 400: Bad Request. El personaje se no se enuentra en la API de marver")
        
        else:
            print("Aqui")
            response_dict = json.loads(respuesta)
            print(response_dict)
            
            name = response_dict["name"]
            image_url = response_dict["image_url"]
            appearances = response_dict["appearances"]
            # print(image_url)
       
            # # Crea un nuevo documento de usuario en la base de datos
            user_id = database.con_bd.users_collection_addToLayaway.insert_one(
                { "comics_name": name,"image_url":image_url,  "appearances": appearances, "username": username}).inserted_id

            return 'Cómic agregado', 201 
    else:
        return 'No se proporcionó un token de autorización', 401


if __name__ == "__main__":
    app.run()
