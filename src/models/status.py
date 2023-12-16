from setup import db, ma 
from marshmallow import fields

# Creates table structure with column names and data types 
class Status(db.Model):
    __tablename__ = 'status'

    title = db.Column(db.String, primary_key=True,)


    jedi = db.relationship('Jedi', back_populates= 'status')

class StatusSchema(ma.Schema):

    class Meta:
        fields = ('title',)

