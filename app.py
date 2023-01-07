import os
from urllib import response
from flask import Flask, jsonify, request
import public.Functions as Functions
# import jwt
import database.con_bd

app = Flask(__name__)


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

# @app.route("/user/<username>", methods=["GET"])
# def get_user_data(username):
#     Comprobar si el usuario está autenticado
#     if not is_authenticated():
#         return jsonify({"message": "No autorizado"}), 401

#     Recuperar la información del usuario de la base de datos
#     user = database.con_bd.users_collection.find_one({"username": username})
#     if not user:
#         return jsonify({"message": "Usuario no encontrado"}), 404

#     Devolver la información del usuario al cliente
#     return jsonify({"username": user["username"], "email": user["email"]})

@app.route("/user/<username>")
def search3(username):
    respuesta = Functions.logged(username)
    return respuesta 

if __name__ == "__main__":
    app.run()
