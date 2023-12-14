from flask import abort
from flask_jwt_extended import get_jwt_identity
from models.jedi import Jedi
from setup import db

def authorize(jedi_id=None):
    jwt_jedi_id = get_jwt_identity()
    stmt = db.select(Jedi).filter_by(id=jwt_jedi_id)
    jedi = db.session.scalar(stmt)
    # If it's not the case that the user is an admin or user_id is truthy and matches the token
    # i.e. if user_id isn't passed in, they must be admin
    if not (jedi.rank = "master" or (jedi_id and jwt_jedi_id == jedi_id)):
        abort(401)