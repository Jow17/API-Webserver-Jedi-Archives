from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from setup import db
from models.planet import PlanetSchema, Planet
from auth import councilmember, master
from sqlalchemy.exc import IntegrityError

planets_bp = Blueprint('planets', __name__, url_prefix='/planets')

# Get all planets 
@planets_bp.route("/")
@jwt_required()
def all_planets():
    stmt = db.select(Planet)  
    planets = db.session.scalars(stmt).all()
    return PlanetSchema(many=True).dump(planets)

# Get one planet
@planets_bp.route('/<string:planet_name>')
@jwt_required()
def one_planet(planet_name):
    stmt = db.select(Planet).filter_by(planet_name=planet_name)
    planet = db.session.scalar(stmt)
    if planet:
        return PlanetSchema().dump(planet)
    else:
        return {'error': 'Planet not found'}, 404

# Register a new planet
@planets_bp.route('/', methods=['POST'])
@jwt_required()
def register_planet():
    master()
    try:
        planet_info = PlanetSchema(exclude=['id']).load(request.json)
        planet = Planet(
            planet_name = planet_info['planet_name'],
            sector = planet_info.get('sector', ''),
            population = planet_info.get('population', ''),
            allegiance = planet_info.get('allegiance', ''),
            description = planet_info["description"],
            jedi_assigned = planet_info.get('jedi_assigned', ''),
            jedi_id=get_jwt_identity()
        )
        db.session.add(planet)
        db.session.commit()
        return PlanetSchema().dump(planet), 201
    except IntegrityError:
        return {"error": "Planet has already been registered!"}, 409

# Update a planet
@planets_bp.route('/<string:planet_name>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_planet(planet_name):
    planet_info = PlanetSchema(exclude=['id']).load(request.json)
    stmt = db.select(Planet).filter_by(planet_name=planet_name)
    planet = db.session.scalar(stmt)
    if planet:
        master(planet.jedi_id)
        planet.allegiance = planet_info.get('allegiance', planet.allegiance)
        planet.jedi_assigned = planet_info.get('jedi_assigned', planet.jedi_assigned)
        db.session.commit()
        return PlanetSchema().dump(planet)
    else:
        return {'error': 'Planet not found'}, 404
    
# Delete a planet
@planets_bp.route('<string:planet_name>', methods=['DELETE'])
@jwt_required()
def delete_planet(planet_name):
    stmt = db.select(Planet).filter_by(planet_name=planet_name)
    planet = db.session.scalar(stmt)
    if planet:
        councilmember()
        db.session.delete(planet)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'Planet not found'}, 404