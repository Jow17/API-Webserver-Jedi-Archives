from setup import db, ma
from marshmallow import fields
from marshmallow.validate import OneOf

VALID_ALLEGIANCES = ('Republic', 'Seperatist', 'Independent' )

# Creates table structure with column names and data types 
class Planet(db.Model):
    __tablename__ = 'planets'

    id = db.Column(db.Integer, primary_key=True)

    planet_name = db.Column(db.String, nullable=False, unique=True)
    sector = db.Column(db.String, nullable=False)
    population = db.Column(db.String)
    allegiance = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)

    jedi_id = db.Column(db.Integer, db.ForeignKey('jedi.id'), nullable=False)
    jedi = db.relationship('Jedi', back_populates='planets') 

# JSON (de)serialization with Marshmallow
class PlanetSchema(ma.Schema):
    jedi = fields.Nested('JediSchema', only=['jedi_name'])
    allegiance= fields.String(required=True, validate=OneOf(VALID_ALLEGIANCES))

    class Meta:
        fields = ('id','planet_name', 'sector', 'population', 'allegiance', 'description','jedi',) 
    


    
    