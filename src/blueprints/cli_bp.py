from flask import Blueprint
from setup import db, bcrypt
from models.jedi import Jedi
from models.planet import Planet
from models.species import Species


db_commands = Blueprint('db', __name__)

@db_commands.cli.command("create")
def db_create():
    db.drop_all()
    db.create_all()
    print("Created tables")

@db_commands.cli.command("seed") 
def db_seed():
    #Jedi 
    jedi = [
        Jedi(
            username="Uncle_Ben57",
            name="Obi-wan Kenobi",
            access_code=bcrypt.generate_password_hash("highground24").decode("utf8"),
            species="Human",
            rank = "Master",
            apprentice = "Anakin Skywalker",
            current_location = "Kamino",
            status = "Alive",
        ),
        Jedi(
            username="Grandmaster01",
            name="Yoda",
            access_code=bcrypt.generate_password_hash("sizemattersnot").decode("utf8"),
            species="Unknown",
            rank = "Councilmember",
            current_location = "Coruscant",
            status = "Alive",
        )
    ]

    db.session.add_all(jedi)
    db.session.commit()

    # Planets
    planets = [
        Planet(
            planet_name="Kamino",
            sector="Abrion",
            population="1 billion",
            allegiance="Independent",
            description="Almost entirely covered by sea, the Kaminoans have build a state of the art cloning facility",
            jedi_assigned = "Obi-Wan Kenobi",
        ),    
        Planet(
            planet_name="Coruscant",
            sector="Corusant", 
            population="trillions",
            allegiance ="Republic",
            description="The center of the galaxy",
        )
    ]
    db.session.add_all(planets)
    db.session.commit()

    # Species
    species = [
        Species(
            species_name = "human",
            designation = "sentient",
            home_planet = "Coruscant",
            lifespan = "80 years",
        )
    ]

    db.session.add_all(species)
    db.session.commit()

print("Database seeded")