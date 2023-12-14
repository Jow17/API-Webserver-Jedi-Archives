from setup import db, ma
from marshmallow import fields
from marshmallow.validate import OneOf

VALID_ALLEGIANCES = ('Republic', 'Seperatist', 'Independent' )

class Planet(db.Model):
    __tablename__ = 'planets'

    id = db.Column(db.Integer, primary_key=True)

    planet_name = db.Column(db.String, nullable=False)
    sector = db.Column(db.String, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    allegiance = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    jedi_assigned = db.Column(db.String)

class Planet_Schema(ma.Schema):
    allegiance = fields.String(validate=OneOf(VALID_ALLEGIANCES))

    class Meta:
        fields = ('planet_name', 'system', 'population', 'allegiance', 'jedi_assigned') 
    


    
    