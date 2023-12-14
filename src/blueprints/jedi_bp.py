from flask import Blueprint, request
from models.jedi import Jedi, JediSchema
from setup import bcrypt, db
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta
# from auth import authorize


jedi_bp = Blueprint('jedi', __name__, url_prefix='/jedi')

@jedi_bp.route("/register", methods=["POST"])
@jwt_required()
def register():
    # authorize() # Admin only
    try:
        # Parse incoming POST body through the schema
        jedi_info = JediSchema(exclude=["id"]).load(request.json)
        # Create a new user with the parsed data
        jedi = Jedi(
            username=jedi_info["username"],
            access_code=bcrypt.generate_password_hash(jedi_info["access_code"]).decode(
                "utf8"
            ),
            name=jedi_info.get("name", ""),
            rank=jedi_info.get("rank", ""),
            master=jedi_info.get("master", ""),
            apprentice=jedi_info.get("apprentice", ""),
            current_location=jedi_info.get("current_location", ""),
            status=jedi_info.get("status", ""),
        )

        # Add and commit the new user to the database
        db.session.add(jedi)
        db.session.commit()

        # Return the new user
        return JediSchema(exclude=["access_code"]).dump(jedi), 201
    except IntegrityError:
        return {"error": "username already in use!"}, 409

@jedi_bp.route("/login", methods=["POST"])
def login():
    # 1. Parse incoming POST body through the schema
    jedi_info = JediSchema(exclude=["id"]).load(request.json)
    # 2. Select jedi with username that matches the one in the POST body
    stmt = db.select(Jedi).where(Jedi.username == jedi_info["username"])
    jedi = db.session.scalar(stmt)
    # 3. Check password hash
    if jedi and bcrypt.check_password_hash(jedi.access_code, jedi_info["access_code"]):
        # 4. Create a JWT token
        token = create_access_token(identity=jedi.id, expires_delta=timedelta(hours=2))
        # 5. Return the token
        return {
            "token": token,
            "jedi": JediSchema(exclude=["id", "access_code","username"]).dump(jedi),
        }
    else:
        return {"error": "Invalid username or access codes!"}, 401

# @jedi_bp.route("/")
# @jwt_required()
# def all_jedi():
#     authorize() # Admin only
#     stmt = db.select(Jedi)
#     users = db.session.scalars(stmt).all()
#     print(users[0].cards)
#     return JediSchema(many=True, exclude=["password"]).dump(jedi)