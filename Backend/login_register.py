from main import *
from models import User

from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
import re


# Register route
@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    # Extract inputs
    username = data.get("username", "").strip()
    email = data.get("email", "").strip()
    password = data.get("password", "")

    EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Basic validation
    if not username or not email or not password:
        return jsonify({"error": "All fields are required", "status_code": 400})

    if not re.match(EMAIL_REGEX, email):
        return jsonify({"error": "Invalid email format", "status_code": 400})

    if len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters", "status_code": 400})

    # Hash password (CRITICAL)
    password_hash = generate_password_hash(password)

    # Create User object
    new_user = User(
        username=username,
        email=email,
        password_hash=password_hash
    )

    try:
        # Save to database
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            "message": "User registered successfully",
            "status_code": 201
        })

    except IntegrityError:
        # Handles duplicate username/email
        db.session.rollback()
        return jsonify({
            "error": "Username or email already exists",
            "status_code": 409
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "error": "Internal server error",
            "status_code": 500
        })
        
        
@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()

        # Extract & sanitize input
        username = data.get("username", "")
        password = data.get("password", "")

        user = User.query.filter_by(username=username).first()

        # Prevent user enumeration
        if not user or not check_password_hash(user.password_hash, password):
            return jsonify({"error": "Invalid username or password", "status_code": 401})

        # Check account status
        if not user.is_active:
            return jsonify({"error": "Account is disabled", "status_code": 403})
        
        # Generate JWT (NO password inside)
        token = jwt.encode(
            {
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=12)
            },
            app.config["SECRET_KEY"],
            algorithm="HS256"
        )

        # Success response (no sensitive data)
        return jsonify({
        "message": "Login successful",
        "status_code":200,
        "token": token,
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role
        }
    })

    except SQLAlchemyError:
        return jsonify({"error": "Database error", "status_code": 500})

    # except Exception:
    #     return jsonify({"error": "Internal server error", "status_code": 500})
        