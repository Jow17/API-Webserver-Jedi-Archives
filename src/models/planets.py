from setup import db, ma
from marshmallow import fields
from marshmallow.validate import OneOf

class Planet(db.Model):
    __tablename__ = 'planets'

    id = db.Column(db.Integer, primary_key=True)

    planet_name = db.Column(db.String, nullable=False)
    system = db.Column(db.String, nullable=False)
    species = db.Column(db.String,)
    population = db.Column(db.integer, nullable=False)
    allegiance = db.Column(db.string, nullable=False)
    jedi_assigned = db.Column(db.string, nullable=False)

class Planet_Schema(ma.Schema):

    class Meta:
        fields = ('plaent_name', 'system', 'species', 'population', 'allegiance', 'jedi_assigned') 
    


    
    