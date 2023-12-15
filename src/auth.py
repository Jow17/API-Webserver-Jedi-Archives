from flask import abort
from flask_jwt_extended import get_jwt_identity
from models.jedi import Jedi
from setup import db

def councilmember(jedi_id=None):
    jwt_jedi_id = get_jwt_identity()
    stmt = db.select(Jedi).filter_by(id=jwt_jedi_id)
    jedi = db.session.scalar(stmt)
    # If it's not the case that the jedi is a councilmember or jedi_id is truthy and matches the token
    # i.e. if jedi_id isn't passed in, they must be a councilmember
    if not (jedi.rank == "Councilmember" or (jedi_id and jwt_jedi_id == jedi_id)):
        abort(401)

def master(jedi_id=None):
    jwt_jedi_id = get_jwt_identity()
    stmt = db.select(Jedi).filter_by(id=jwt_jedi_id)
    jedi = db.session.scalar(stmt)
    # If it's not the case that the jedi is a councilmember or jedi_id is truthy and matches the token
    # i.e. if jedi_id isn't passed in, they must be a councilmember
    if not (jedi.rank == "Master" or "Councilmember" or (jedi_id and jwt_jedi_id == jedi_id)):
        abort(401)