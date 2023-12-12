from flask import Blueprint, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from setup import db
from models.jedi import CardSchema, Jedi
from auth import authorize

jedi_bp = Blueprint('jedi', __name__, url_prefix='/jedi')

@jedi_bp.route("/")
@jwt_required()
def all_jedi():
    stmt = db.select(
        Jedi 
    )