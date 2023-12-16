from flask import abort
from flask_jwt_extended import get_jwt_identity
from models.jedi import Jedi
from setup import db

# Checks if jedi's rank is councilmember 
def councilmember(jedi_id=None):
    jwt_jedi_id = get_jwt_identity()
    stmt = db.select(Jedi).filter_by(id=jwt_jedi_id)
    jedi = db.session.scalar(stmt)
    if not (jedi.rank == "Councilmember"):
        abort(401)

# Checks if jedi's rank is master
def master(jedi_id=None):
    jwt_jedi_id = get_jwt_identity()
    stmt = db.select(Jedi).filter_by(id=jwt_jedi_id)
    jedi = db.session.scalar(stmt)
    if not (jedi.rank == "Master" or "Councilmember"):
        abort(401)