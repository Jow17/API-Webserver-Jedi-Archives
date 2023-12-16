from setup import db, ma 
from marshmallow import fields 
from marshmallow.validate import OneOf

VALID_DESIGNATIONS = ('Sentient' , 'Non-sentient', 'Semi-sentient')

# Creates table structure with column names and data types 
class Species(db.Model):
    __tablename__ = 'species'

    id = db.Column(db.Integer, primary_key=True)

    species_name = db.Column(db.String, nullable=False)
    designation = db.Column(db.String, nullable=False)
    lifespan = db.Column(db.String)

    jedi_id = db.Column(db.Integer, db.ForeignKey('jedi.id'), nullable=False)
    jedi = db.relationship('Jedi', back_populates='species')

# Converts datatypes into JSON  
class SpeciesSchema(ma.Schema):
    designation = fields.String(validate=OneOf(VALID_DESIGNATIONS))

    class Meta:
        fields = ('id', 'species_name', 'designation', 'lifespan', 'jedi_id',)

