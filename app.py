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


@app.route("/register", methods=["POST"])
def register():
    
    # obtener el cuerpo de una solicitud HTTP
    data = request.get_json()
    return Functions.register_user(data)
    # if Functions.register_user(data):
    #     return data["user_id"]
    # else:
    #     return 'Usuario no registrado'
    



if __name__ == "__main__":
    app.run()
