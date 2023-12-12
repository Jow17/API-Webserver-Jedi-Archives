from setup import db, ma
from marshmallow import fields
from marshmallow.validate import OneOf

class Jedi(db.Model):
    __tablename__ = 'jedi'

    jedi_id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)
    access_code = db.Column(db.String, nullable=False)
    rank = db.Column(db.String, nullable=False)
    master = db.Column(db.String, nullable=True)
    apprentice = db.Column(db.String, nullable=True)
    location = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)

    species_name = db.Column(db.String, db.ForeignKey('species.name'), nullable=False)

class JediSchema(ma.Schema):
    

    

