from setup import db, ma
from marshmallow import fields
from marshmallow.validate import OneOf

VALID_ALLEGIANCES = ('Republic', 'Seperatist', 'Independent' )

class Planet(db.Model):
    __tablename__ = 'planets'

    id = db.Column(db.Integer, primary_key=True)

    planet_name = db.Column(db.String, nullable=False)
    sector = db.Column(db.String, nullable=False)
    population = db.Column(db.integer, nullable=False)
    allegiance = db.Column(db.string, nullable=False)
    description = db.Column(db.text, nullable=False)
    jedi_assigned = db.Column(db.string)

class Planet_Schema(ma.Schema):
    allegiance = fields.String(validate=OneOf(VALID_ALLEGIANCES))

    class Meta:
        fields = ('planet_name', 'system', 'population', 'allegiance', 'jedi_assigned') 
    


    
    