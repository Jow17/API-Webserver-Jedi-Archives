from setup import db, ma 

class Jedi(db.Model):
    __tablename__ = 'Jedi'

    jedi_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)
    

