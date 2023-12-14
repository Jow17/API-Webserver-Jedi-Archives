from flask import Blueprint, request
from models.jedi import Jedi, JediSchema
from setup import bcrypt, db
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta
# from auth import authorize


jedi_bp = Blueprint('jedi', __name__, url_prefix='/jedi')

@jedi_bp.route("/login", methods=["POST"])
def login():
    # 1. Parse incoming POST body through the schema
    jedi_info = JediSchema(exclude=["id"]).load(request.json)
    # 2. Select user with email that matches the one in the POST body
    stmt = db.select(Jedi).where(Jedi.first_name == jedi_info["first_name"])
    jedi = db.session.scalar(stmt)
    # 3. Check password hash
    if jedi and bcrypt.check_password_hash(jedi.access_code, jedi_info["access_code"]):
        # 4. Create a JWT token
        token = create_access_token(identity=jedi.id, expires_delta=timedelta(hours=2))
        # 5. Return the token
        return {
            "token": token,
            "user": JediSchema(exclude=["password", "cards"]).dump(jedi),
        }
    else:
        return {"error": "Invalid Jedi or access codes!"}, 401
