from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from setup import db
from models.planet import PlanetSchema, Planet
from auth import councilmember, master

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
    councilmember()
    planet_info = PlanetSchema(exclude=['id']).load(request.json)
    planet = Planet(
        planet_name = planet_info('planet_name', ''),
        sector = planet_info.get('sector', ''),
        population = planet_info.get('population', ''),
        allegiance = planet_info.get('allegiance', ''),
        description = planet_info.get('description', ''),
        jedi_assigned = planet_info.get('jedi_assigned' ''),
        jedi_id = get_jwt_identity()
    )
    db.session.add(planet)
    db.session.commit()
    return PlanetSchema().dump(planet), 201

# Update a planet
@planets_bp.route('/<string:planet_name>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_planet(planet_name):
    (master)
    planet_info = PlanetSchema(exclude=['id']).load(request.json)
    stmt = db.select(Planet).filter_by(planet_name=planet_name)
    planet = db.session.scalar(stmt)
    if planet:
        master(planet.jedi_id)
        planet.allegiance = planet_info.get('allegiance', planet.allegiance)
        planet.jedi_assigned = planet_info.get('description', planet.jedi_assigned)
        db.session.commit()
        return PlanetSchema().dump(planet)
    else:
        return {'error': 'Planet not found'}, 404

@planets_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_planet(planet_name):
    master()
    stmt = db.select(Planet).filter_by(planet_name=planet_name)
    planet = db.session.scalar(stmt)
    if planet:
        councilmember()
        db.session.delete(planet)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'Planet not found'}, 404