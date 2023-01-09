import datetime
from distutils import config
import json
import logging
from urllib import response
from bson import ObjectId
from flask import Flask, abort, appcontext_popped, jsonify, request
import requests
import hashlib
import database.con_bd
import jwt

app = Flask(__name__)
app.config["SECRET_KEY"] = "mi_clave_secreta"
# Configurar el sistema de registro

# Establezca el tiempo de la solicitud (ts), la clave privada (privateKey) y la clave pública (publicKey)
ts = "1"
# Reemplace YYYY con su clave privada
private_key = "b35fa159385fb6443459bf90ad8477ebece67010"
# Reemplace XXXX con su clave pública
public_key = "755c14df1f81387f1d83be92d9445371"
# Concatene ts, privateKey y publicKey en una sola cadena
string = ts + private_key + public_key
# Genere el hash MD5 de la cadena
hash = hashlib.md5(string.encode('utf-8')).hexdigest()
# print(hash)

# busqueda por caracteres


def comics(keyword):
    # Establezca el URL de la API de Marvel
    url = "https://gateway.marvel.com/v1/public/comics"
    params = {
        "apikey": public_key,
        "ts": ts,
        "hash": hash,
        "titleStartsWith": keyword
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:

        data = response.json()["data"]
        comic = data["results"][0]

        comic_id = comic["id"]
        title = comic["title"]
        image_url = comic["thumbnail"]["path"] + \
            "." + comic["thumbnail"]["extension"]

        on_sale_date = comic["dates"][0]["date"]

        comic_data = {
            "id": comic_id,
            "title": title,
            "image_url": image_url,
            "on_sale_date": on_sale_date
        }
        json_data = json.dumps(comic_data)
        return json_data
    else:
        raise Exception("Request failed with status code:",
                        response.status_code)


def characters(keyword):
    api_url = "https://gateway.marvel.com/v1/public/characters"
    # Establezca los parámetros de la solicitud
    params = {
        "apikey": public_key,
        "ts": ts,
        "hash": hash,
        "nameStartsWith": keyword
    }
    # Haga la solicitud a la API
    response = requests.get(api_url, params=params)
    try:
        if response.status_code == 200:

            data = response.json()["data"]
            character = data["results"][0]

            character_id = character["id"]
            name = character["name"]
            image_url = character["thumbnail"]["path"] + \
                "." + character["thumbnail"]["extension"]
            appearances = character["comics"]["available"]

            character_data = {
                "id": character_id,
                "name": name,
                "image_url": image_url,
                "appearances": appearances
            }
            json_data = json.dumps(character_data)
            return json_data 
    except Exception as e:
        return "Error 400: Bad Request. El personaje se no se enuentra en la API de marver" ,400


def get_all_personaje():
    # page_size es el número de resultados que se devuelven en cada página. Por ejemplo, si page_size es 20, cada página de resultados contendrá 20 resultados.
    # total_results es el número total de resultados que se esperan obtener de la API. Esto se utiliza para calcular el número total de páginas necesarias para obtener todos los resultados.
    # num_pages es el número total de páginas que se necesitan para obtener todos los resultados. Se calcula dividiendo total_results entre page_size y, si hay un resto, se agrega una página adicional.
    # El ciclo for itera sobre el número de páginas necesarias para obtener todos los resultados. En cada iteración, se establece el valor de offset para la solicitud a la API y se realiza la solicitud. Los resultados se procesan y se agrega cada resultado a la lista characters. Al final del ciclo, characters contendrá todos los resultados.
    api_url = "https://gateway.marvel.com/v1/public/characters"

    # Establece el número de resultados por página
    page_size = 10

    # Establece el número total de resultados
    total_results = 100

    # Calcula el número total de páginas
    num_pages = total_results // page_size
    if total_results % page_size > 0:
        num_pages += 1

    # Realiza una solicitud a la API por cada página
    characters = []
    for i in range(num_pages):
        offset = i * page_size

        # Establece los parámetros de la solicitud
        params = {
            "apikey": public_key,
            "ts": ts,
            "hash": hash,
            "offset": offset
        }

        # Hace la solicitud a la API
        response = requests.get(api_url, params=params)

        # Procesa la respuesta de la API
        if response.status_code == 200:
            data = response.json()["data"]

            for character in data["results"]:
                character_id = character["id"]
                name = character["name"]
                image_url = character["thumbnail"]["path"] + \
                    "." + character["thumbnail"]["extension"]
                appearances = character["comics"]["available"]

                character_data = {
                    "id": character_id,
                    "name": name,
                    "image_url": image_url,
                    "appearances": appearances
                }

                characters.append(character_data)
        else:
            print("Request failed with status code:", response.status_code)

    json_data = json.dumps(characters)
    return json_data


def get_all_comics():
    # page_size es el número de resultados que se devuelven en cada página. Por ejemplo, si page_size es 20, cada página de resultados contendrá 20 resultados.
    # total_results es el número total de resultados que se esperan obtener de la API. Esto se utiliza para calcular el número total de páginas necesarias para obtener todos los resultados.
    # num_pages es el número total de páginas que se necesitan para obtener todos los resultados. Se calcula dividiendo total_results entre page_size y, si hay un resto, se agrega una página adicional.
    # El ciclo for itera sobre el número de páginas necesarias para obtener todos los resultados. En cada iteración, se establece el valor de offset para la solicitud a la API y se realiza la solicitud. Los resultados se procesan y se agrega cada resultado a la lista characters. Al final del ciclo, characters contendrá todos los resultados.
    url = "https://gateway.marvel.com/v1/public/comics"

    # Establece el número de resultados por página
    page_size = 10

    # Establece el número total de resultados
    total_results = 100

    # Calcula el número total de páginas
    num_pages = total_results // page_size
    if total_results % page_size > 0:
        num_pages += 1

    # Realiza una solicitud a la API por cada página
    characters = []
    for i in range(num_pages):
        offset = i * page_size

        # Establece los parámetros de la solicitud
        params = {
            "apikey": public_key,
            "ts": ts,
            "hash": hash,
            "offset": offset
        }

        # Hace la solicitud a la API
        response = requests.get(url, params=params)

        # Procesa la respuesta de la API
        if response.status_code == 200:
            data = response.json()["data"]

            for comic in data["results"]:
                comic_id = comic["id"]
                title = comic["title"]
                image_url = comic["thumbnail"]["path"] + \
                    "." + comic["thumbnail"]["extension"]
                on_sale_date = comic["dates"][0]["date"]

                comic_data = {
                    "id": comic_id,
                    "title": title,
                    "image_url": image_url,
                    "on_sale_date": on_sale_date
                }

                characters.append(comic_data)
        else:
            print("Request failed with status code:", response.status_code)

    json_data = json.dumps(characters)
    return json_data


def register_user(data):
    try:
        # Recupera el nombre de usuario y la contraseña del cuerpo de la solicitud
        username = data["username"]
        password = data["password"]
        age = data["age"]

        # Crea un nuevo documento de usuario en la base de datos
        user_id = database.con_bd.users_collection.insert_one(
            {"username": username, "password": password, "age": age}).inserted_id

        # Valida que el ID del documento insertado no esté vacío
        if user_id is not None:
            # El documento se ha insertado con éxito
            return jsonify({"user_id": str(user_id)})
    except Exception as e:
        return jsonify(str(e))


def auth(data):
    try:
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        if all([username, password]):
            user = database.con_bd.users_collection.find_one(
                {"username": username})
            # print("respuesta" + str(user))
            if not user or user["password"] != password:
                return jsonify({"message": "Credenciales inválidas"}), 401

            # Generar un token JWT para el usuario
            token = jwt.encode({
                "username": username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }, app.config["SECRET_KEY"])
            # print(token)

            # _id = user["_id"]
            username = user["username"]
            password = user["password"]
            age = user["age"]
            token = token
            # Crea un nuevo documento de usuario en la base de datos
            user_id = database.con_bd.users_collection_token.insert_one(
                {"username": username, "password": password, "age": age, "token": token}).inserted_id

            if user_id is not None:
                # Devolver el token generado al usuario
                return jsonify({"token": token})
        else:
            return jsonify({"message": "El nombre de usuario o la contraseña están vacíos"})

    except Exception as e:
        return jsonify(str(e))


def logged(username):
    try:

        if all([username]):
            user = database.con_bd.users_collection_token.find_one(
                {"username": username})
            print("respuesta" + str(user))

            if user is None:
              return jsonify({"message": "Usuario no se encuentra en autenticado"}), 401
            else:
                # Crear un diccionario con el nombre y la edad del usuario
                print(user["_id"])
                object_id = ObjectId( user["_id"])
                json_object_id = json.dumps(str(object_id))
                cleaned_string = json_object_id.replace('"', '')
                user_data = {"id":cleaned_string,"name": user["username"],
                            "age": user["age"], "token": user["token"]}

                return json.dumps(user_data)

    except Exception as e:
        return jsonify(str(e))


