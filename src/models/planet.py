from setup import db, ma
from marshmallow import fields
from marshmallow.validate import OneOf

VALID_ALLEGIANCES = ('Republic', 'Seperatist', 'Independent' )

class Planet(db.Model):
    __tablename__ = 'planets'

    id = db.Column(db.Integer, primary_key=True)

    planet_name = db.Column(db.String, nullable=False, unique=True)
    sector = db.Column(db.String, nullable=False)
    population = db.Column(db.String)
    allegiance = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    jedi_assigned = db.Column(db.String)

    jedi_id = db.Column(db.Integer, db.ForeignKey('jedi.id'), nullable=False)


class PlanetSchema(ma.Schema):
    jedi = fields.Nested('JediSchema', exclude=['access_code'])
    allegiance= fields.String(required=True, validate=OneOf(VALID_ALLEGIANCES))

    class Meta:
        fields = ('id','planet_name', 'sector', 'population', 'allegiance', 'description', 'jedi_id', 'jedi_assigned') 
    


    
    