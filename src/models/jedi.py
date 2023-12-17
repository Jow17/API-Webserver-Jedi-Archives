from setup import db, ma
from marshmallow import fields
from marshmallow.validate import Length

# Creates table structure with column names and data types 
class Jedi(db.Model):
    __tablename__ = 'jedi'

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String, nullable=False, unique=True)
    access_code = db.Column(db.String, nullable=False)
    jedi_name = db.Column(db.String, nullable=False, unique=True)
    current_location = db.Column(db.Text, nullable=False)
    species_name = db.Column(db.String, nullable=False)
    
    rank_title = db.Column(db.String, db.ForeignKey('ranks.title'), nullable=False)
    rank = db.relationship('Rank', back_populates='jedi')

    status_title = db.Column(db.String, db.ForeignKey('statuses.title'), nullable=False)
    statuses = db.relationship('Status', back_populates='jedi')

    species = db.relationship('Species', back_populates='jedi')

    planets = db.relationship('Planet', back_populates='jedi')
    

# JSON (de)serialization with Marshmallow
class JediSchema(ma.Schema):
    rank = fields.Nested('RankSchema')
    statuses = fields.Nested('StatusSchema')
    username = fields.String(validate=Length(min=6, error = 'Username must be at least 6 characters'))
    access_code = fields.String(validate=Length(min=8, error = 'Access code must be as least 8 characers long'))
    
    class Meta:
        fields = ("id", "username","access_code", "jedi_name", "current_location", "species_name", "rank_title", "status_title",)
    

    

