from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from setup import db
from models.species import SpeciesSchema, Species
from auth import councilmember, master
from sqlalchemy.exc import IntegrityError

species_bp = Blueprint('species',__name__, url_prefix='/species')

# Get all species 
@species_bp.route("/")
@jwt_required()
def all_species():
    # select * from species;
    stmt = db.select(Species)
    species = db.session.scalars(stmt).all()
    return SpeciesSchema(many=True).dump(species)

# Get one species
@species_bp.route('/<string:species_name>')
@jwt_required()
def one_species(species_name):
    stmt = db.select(Species).filter_by(species_name=species_name)
    species = db.session.scalar(stmt)
    if species:
        return SpeciesSchema().dump(species)
    else:
        return {'error': 'Species not found'}, 404

# Register a new species
@species_bp.route('/', methods=['POST'])
@jwt_required()
def register_species():
    master()
    try:
        species_info = SpeciesSchema(exclude=['id']).load(request.json)
        species = Species(
            species_name = species_info['species_name'],
            designation = species_info.get('designation', ''),
            home_planet = species_info.get('home_planet', ''),
            lifespan = species_info.get('lifespan', ''),
            jedi_id = get_jwt_identity()
        )
        db.session.add(species)
        db.session.commit()
        return SpeciesSchema().dump(species), 201
    except IntegrityError:
        return {"error": "Species has already been registered!"}, 409

# Update a species
@species_bp.route('/<string:species_name>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_species(species_name):
    species_info = SpeciesSchema(exclude=['id']).load(request.json)
    stmt = db.select(Species).filter_by(species_name=species_name)
    species = db.session.scalar(stmt)
    if species:
        master(species.jedi_id)
        species.home_planet = species_info.get('home_planet', species.home_planet)
        species.designation = species_info.get('designation', species.designation)
        db.session.commit()
        return SpeciesSchema().dump(species)
    else:
        return {'error': 'Species not found'}, 404
    
# Delete a species from the database
@species_bp.route('/<string:species_name>', methods=['DELETE'])
@jwt_required()
def delete_species(species_name):
    stmt = db.select(Species).filter_by(species_name=species_name)
    species = db.session.scalar(stmt)
    if species:
        councilmember()
        db.session.delete(species)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'Species not found'}, 404
