from setup import db, ma 

# Creates table structure with column names and data types 
class Rank(db.Model):
    __tablename__ = 'ranks'

    title = db.Column(db.String, primary_key=True, unique=True)

    jedi = db.relationship('Jedi', back_populates= 'rank')


# JSON (de)serialization with Marshmallow
class RankSchema(ma.Schema):

    class Meta:
        fields = ('title',)

