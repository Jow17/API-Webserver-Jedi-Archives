from setup import db,ma 
from marshmallow import fields 
from marshmallow.validate import OneOf

class Species(db.Model):
    __tablename__ = 'species'

    id = db.Column(db.Integer, primary_key=True)

    species_name = db.Column(db.String, nullable=False)
    home_planet = db.Column(db.String, nullable=False)
    lifespan = db.Column(db.String, nullable=False)

class SpeciesSchema(ma.Schema):

    class Meta:
        field = ('species_name', 'home_planet', 'lifespan')

