from flask import Flask, request, jsonify, session
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
import jwt, time, threading
import datetime
from models import db, UserPreferences
from termcolor import colored

app = Flask(__name__)
app.config["SECRET_KEY"] = "d3f8a6a8e24c4c3ea7f9b9c4e7a113cf4eb839927e6a5f761f2ce94804bc9e78"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
CORS(app)
    
# initialising the database
db.init_app(app)

with app.app_context():
    db.create_all()
    print("Database and tables created!")
    
    
def verify_token():
    token = None
    print(request.headers)
    if "Authorization" in request.headers and len(request.headers["Authorization"].split()) == 2: # [bearer, token]
        token = request.headers["Authorization"].split()[1]
    if not token:
        return None, jsonify({"message": "Token is missing!"}), 401
    try:
        data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        print(colored(data, 'green'))
        user_id = data["user_id"]
        return user_id, None, None
    except:
        return None, jsonify({"message": "Token is invalid!"}), 403
        

@app.route("/verify_token", methods=["GET"])
def verify_token_():
    token = None
    print(request.headers)
    
    try:
        if "Authorization" in request.headers and len(request.headers["Authorization"].split()) == 2: # [bearer, token]
            token = request.headers["Authorization"].split()[1]
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            print(colored(data, 'green'))
            user_id = data["user_id"]
            username = data["username"]
            email = data["email"]
            if user_id:
                return jsonify({"message": "Token is valid!",
                                "user": username,
                                "email": email,
                                "status_code": 200})
    except:
        return jsonify({"message": "Token is invalid!",
                        "status_code": 401})

@app.route("/user/preferences", methods=["POST"])
def save_preferences():
    user_id, error_response, status_code = verify_token()
    if status_code == 401:
        return jsonify({
            "status_code": 401,
            "message": "Token is missing!"
        })
    elif status_code == 403:
        return jsonify({
            "status_code": 403,
            "message": "Token is invalid!"
        })
    else:
        # user_id = get_jwt_identity()
        data = request.json

        prefs = UserPreferences.query.filter_by(user_id=user_id).first()

        if not prefs:
            prefs = UserPreferences(user_id=user_id)
            db.session.add(prefs)

        prefs.learning_style = data.get("learning_style", prefs.learning_style)
        prefs.difficulty_level = data.get("difficulty_level", prefs.difficulty_level)
        prefs.daily_goal_minutes = data.get("daily_goal_minutes", prefs.daily_goal_minutes)
        prefs.preferred_task = data.get("preferred_task", prefs.preferred_task)

        db.session.commit()
        return jsonify({"message": "Preferences saved successfully"})
    
@app.route("/user/preferences", methods=["GET"])
def get_preferences():
    user_id, error_response, status_code = verify_token()

    prefs = UserPreferences.query.filter_by(user_id=user_id).first()
    if not prefs:
        return jsonify({"message": "Preferences not set", "status_code":404})

    return jsonify({
        "learning_style": prefs.learning_style,
        "difficulty_level": prefs.difficulty_level,
        "daily_goal_minutes": prefs.daily_goal_minutes,
        "preferred_task": prefs.preferred_task,
        "status_code":200
    })
    

if __name__ == "__main__":
    from login_register import *  # just want to keep login/register methods in another file
    from process_prompts import *  # just want to keep processing prompt and generating output methods in another file
    
    print('Total threads: {}'.format(threading.active_count()))
    
    app.run(debug=True, use_reloader=True)

