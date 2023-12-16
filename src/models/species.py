from setup import db, ma 
from marshmallow import fields 
from marshmallow.validate import OneOf

VALID_DESIGNATIONS = ('Sentient' , 'Non-sentient', 'Semi-sentient')

# Creates table structure with column names and data types 
class Species(db.Model):
    __tablename__ = 'species'

    id = db.Column(db.Integer, primary_key=True)

    species_name = db.Column(db.String, nullable=False, unique=True)
    designation = db.Column(db.String, nullable=False)
    home_planet = db.Column(db.String)
    lifespan = db.Column(db.String)

    jedi_id = db.Column(db.Integer, db.ForeignKey('jedi.id'), nullable=False)

# Converts datatypes into JSON  
class SpeciesSchema(ma.Schema):
    designation = fields.String(validate=OneOf(VALID_DESIGNATIONS))

    class Meta:
        fields = ('id', 'species_name', 'designation', 'home_planet', 'lifespan', 'jedi', 'jedi_id')

