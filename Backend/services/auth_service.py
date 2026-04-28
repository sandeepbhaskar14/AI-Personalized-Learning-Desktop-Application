from flask import request, jsonify, current_app
from termcolor import colored
import jwt


def verify_token():
    token = None
    print(request.headers)
    if "Authorization" in request.headers and len(request.headers["Authorization"].split()) == 2: # [bearer, token]
        token = request.headers["Authorization"].split()[1]
    if not token:
        return None, jsonify({"message": "Token is missing!"}), 401
    try:
        data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
        print(colored(data, 'green'))
        user_id = data["user_id"]
        return user_id, None, None
    except:
        return None, jsonify({"message": "Token is invalid!"}), 403