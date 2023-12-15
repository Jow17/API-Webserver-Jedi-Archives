from setup import db, ma
from marshmallow import fields
from marshmallow.validate import OneOf, Length

VALID_STATUSES = ('Alive', 'Deceased', 'Unknown')
VALID_RANKS = ('Councilmember', 'Master', 'Knight', 'Padawan')

class Jedi(db.Model):
    __tablename__ = 'jedi'

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    access_code = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    rank = db.Column(db.String, nullable=False)
    master = db.Column(db.String)
    apprentice = db.Column(db.String)
    current_location = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)

    planets = db.relationship('Planet', back_populates='jedi')
    species = db.relationship('Species', back_populates='jedi')

    

class JediSchema(ma.Schema):
    status = fields.String(validate=OneOf(VALID_STATUSES))
    rank = fields.String(validate=OneOf(VALID_RANKS))
    username = fields.String(required=True)
    access_code = fields.String(required=True, validate=Length(min=8, error = 'Access code must be as least 8 characers long'))
    
 
    class Meta:
        fields = ("id", "username", "name", "access_code", "species", "rank", "master", "apprentice","current_location", "status")
    

    

