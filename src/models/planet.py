from setup import db, ma
from marshmallow import fields
from marshmallow.validate import OneOf

VALID_ALLEGIANCES = ('Republic', 'Seperatist', 'Independent' )

class Planet(db.Model):
    __tablename__ = 'planets'

    id = db.Column(db.Integer, primary_key=True)

    planet_name = db.Column(db.String, nullable=False)
    sector = db.Column(db.String, nullable=False)
    population = db.Column(db.String, nullable=False)
    allegiance = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    jedi_assigned = db.Column(db.String)

    jedi_id = db.Column(db.Integer, db.ForeignKey('jedi.id'), nullable=False)
    jedi = db.relationship('Jedi', back_populates='planets')


class PlanetSchema(ma.Schema):
    allegiance = fields.String(validate=OneOf(VALID_ALLEGIANCES))

    class Meta:
        fields = ('planet_name', 'system', 'population', 'allegiance', 'jedi_assigned') 
    


    
    