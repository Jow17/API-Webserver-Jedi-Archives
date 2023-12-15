from setup import db,ma 
from marshmallow import fields 
from marshmallow.validate import OneOf

VALID_DESIGNATIONS = ('sentient' , 'non-sentient', 'semi-sentient')


class Species(db.Model):
    __tablename__ = 'species'

    id = db.Column(db.Integer, primary_key=True)

    species_name = db.Column(db.String, nullable=False)
    designation = db.Column(db.String, nullable=False)
    home_planet = db.Column(db.String)
    lifespan = db.Column(db.String, nullable=False)

    jedi_id = db.Column(db.Integer, db.ForeignKey('jedi.id'), nullable=False)
    jedi = db.relationship('Jedi', back_populates='species')
class SpeciesSchema(ma.Schema):
    designation = fields.String(validate=OneOf(VALID_DESIGNATIONS))

    class Meta:
        field = ('species_name', 'home_planet', 'lifespan')

