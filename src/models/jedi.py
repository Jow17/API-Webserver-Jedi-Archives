from setup import db, ma
from marshmallow import fields
from marshmallow.validate import OneOf

VALID_STATUSES = ('Alive', 'Deceased', 'Unknown')
VALID_RANKS = ('Councilmember', 'Master', 'Knight', 'Padawan')

class Jedi(db.Model):
    __tablename__ = 'jedi'

    jedi_id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)
    access_code = db.Column(db.String, nullable=False)
    rank = db.Column(db.String, nullable=False)
    master = db.Column(db.String)
    apprentice = db.Column(db.String)
    location = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)

    # species_name = db.Column(db.String, db.ForeignKey('species.name'), nullable=False)

class JediSchema(ma.Schema):
    jedi = fields.Nested('JediSchema', exclude=['access_code'])
    status = fields.String(validate=OneOf(VALID_STATUSES))
    rank = fields.Integer(validate=OneOf(VALID_RANKS))
 
    class Meta:
        field = ("first_name", "last_name","rank", "master", "apprentice","location", "status")
    

    

