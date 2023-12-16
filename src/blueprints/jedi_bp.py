from flask import Blueprint, request
from models.jedi import Jedi, JediSchema
from setup import bcrypt, db
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta
from auth import councilmember, master

jedi_bp = Blueprint('jedi', __name__, url_prefix='/jedi')


# Register a Jedi
@jedi_bp.route("/register", methods=["POST"])
@jwt_required()
def register():
    councilmember() 
    try:
        jedi_info = JediSchema(exclude=["id"]).load(request.json)
        jedi = Jedi(
            username=jedi_info["username"],
            access_code=bcrypt.generate_password_hash(jedi_info["access_code"]).decode(
                "utf8"
            ),
            name=jedi_info.get("name", ""),
            rank=jedi_info.get("rank", ""),
            species_name=jedi_info.get("species", ""),
            master=jedi_info.get("master", ""),
            apprentice=jedi_info.get("apprentice", ""),
            current_location=jedi_info.get("current_location", ""),
            status=jedi_info.get("status", ""),
        )

        db.session.add(jedi)
        db.session.commit()

        return JediSchema(exclude=["access_code"]).dump(jedi), 201
    except IntegrityError:
        return {"error": "username already in use!"}, 409

# Login a Jedi
@jedi_bp.route("/login", methods=["POST"])
def login():
    jedi_info = JediSchema(exclude=["id"]).load(request.json)
    stmt = db.select(Jedi).where(Jedi.username == jedi_info["username"])
    jedi = db.session.scalar(stmt)
    if jedi and bcrypt.check_password_hash(jedi.access_code, jedi_info["access_code"]):
        token = create_access_token(identity=jedi.id, expires_delta=timedelta(hours=2))
        return {
            "token": token,
            "jedi": JediSchema(exclude=["id", "access_code",]).dump(jedi),
        }
    else:
        return {"error": "Invalid username or access codes!"}, 401

# Update a Jedi's current location and status
@jedi_bp.route('/<string:name>/update', methods=['PUT', 'PATCH'])
@jwt_required()
def update_jedi(name):
    jedi_info = JediSchema(exclude=['id']).load(request.json)
    stmt = db.select(Jedi).filter_by(name=name) 
    jedi = db.session.scalar(stmt)
    if jedi:
        master, councilmember(jedi.name)
        jedi.current_location = jedi_info.get('current_location', jedi.current_location)
        jedi.status = jedi_info.get('status', jedi.status)
        db.session.commit()
        return JediSchema(only=['name', 'current_location', 'status']).dump(jedi)
    else:
        return {'error': 'Jedi not found'}, 404

# Update a Jedi's rank
@jedi_bp.route('/<string:name>/update/rank', methods=['PUT', 'PATCH'])
@jwt_required()
def update_jedi_rank(name):
    jedi_info = JediSchema(exclude=['id']).load(request.json)
    stmt = db.select(Jedi).filter_by(name=name) 
    jedi = db.session.scalar(stmt)
    if jedi:
        councilmember(jedi.name)
        jedi.rank = jedi_info.get('rank', jedi.rank)
        db.session.commit()
        return JediSchema(only=['name', 'rank']).dump(jedi)
    else:
        return {'error': 'Jedi not found'}, 404

# Get one Jedi
@jedi_bp.route('/<string:name>')
@jwt_required()
def one_jedi(name):
    stmt = db.select(Jedi).filter_by(name=name)
    jedi = db.session.scalar(stmt)
    if jedi:
        return JediSchema(exclude=['access_code', 'id', 'username']).dump(jedi)
    else:
        return {'error': 'Jedi not found'}, 404

# Get all Jedi
@jedi_bp.route("/", methods=['GET'])
@jwt_required()
def all_jedi():
    master, councilmember()
    stmt = db.select(Jedi)
    jedi = db.session.scalars(stmt).all()
    return JediSchema(many=True, exclude=['access_code']).dump(jedi)
