from flask import Blueprint, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from setup import db
from models.planet import PlanetSchema, Planet
from auth import authorize 

planets_bp = Blueprint('planets', __name__, url_prefix='/planets')

# Get all planets 
@planets_bp.route("/")
@jwt_required()
def all_planets():
    # select * from planets;
    stmt = db.select(
        Planet
    )  # .where(db.or_(Card.status != 'Done', Card.id > 2)).order_by(Card.title.desc())
    planets = db.session.scalars(stmt).all()
    return PlanetSchema(many=True).dump(planets)

# Get one card
@planets_bp.route('/<string:planet_name>')
@jwt_required()
def one_planet(planet_name):
    stmt = db.select(Planet).filter_by(planet_name=planet_name) # .where(Card.id == id)
    planet = db.session.scalar(stmt)
    if planet:
        return PlanetSchema().dump(planet)
    else:
        return {'error': 'Planet not found'}, 404
    



