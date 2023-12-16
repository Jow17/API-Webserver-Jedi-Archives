from flask import Blueprint
from setup import db, bcrypt
from models.jedi import Jedi
from models.planet import Planet
from models.species import Species


db_commands = Blueprint('db', __name__)

# Drops all tables and then creates all tables
@db_commands.cli.command("create")
def db_create():
    db.drop_all()
    db.create_all()
    print("Created tables")

# Adds data to the database table columns
@db_commands.cli.command("seed") 
def db_seed():
    jedi = [
        Jedi(
            id = 0,
            username="Grandmaster01",
            jedi_name="Yoda",
            access_code=bcrypt.generate_password_hash("sizemattersnot").decode("utf8"),
            rank = "Councilmember",
            species = "Unknown",
            current_location = "Coruscant",
            status = "Alive",
        ),
        Jedi(
            username="Uncle_Ben",
            jedi_name="Obi-wan_Kenobi",
            access_code=bcrypt.generate_password_hash("highground24").decode("utf8"),
            rank = "Master",
            species = "Human",
            apprentice = "Anakin_Skywalker",
            current_location = "Kamino",
            status = "Alive",
        ),
        Jedi(
            username="Chosen_1",
            jedi_name="Anakin_Skywalker",
            access_code=bcrypt.generate_password_hash("Idontlikesand").decode("utf8"),
            rank = "Knight",
            species = "Human",
            master = "Obi-wan_Kenobi",
            current_location = "Tatooine",
            status = "Alive",
        ),
    ]

    db.session.add_all(jedi)
    db.session.commit()
    planets = [
        Planet(
            planet_name="Coruscant",
            sector="Corusant", 
            population="Trillions",
            allegiance ="Republic",
            description="The center of the galaxy",
            jedi_id = jedi[0].id
        ),
        Planet(
            planet_name="Kamino",
            sector="Abrion",
            population="1 billion",
            allegiance="Independent",
            description="Almost entirely covered by sea, the Kaminoans have built a state of the art cloning facility",
            jedi_assigned = "Obi-Wan Kenobi",
            jedi_id = jedi[1].id
        ),
    ]

    db.session.add_all(planets)
    db.session.commit()

    # Species
    species = [
        Species(
            species_name = "Human",
            designation = "Sentient",
            home_planet = "Coruscant",
            lifespan = "80 years",
            jedi_id = jedi[1].id
        ),
        Species(
            species_name = "Kaminoan",
            designation = "Sentient",
            home_planet = "Kamino",
            lifespan = "80 years",
            jedi_id = jedi[2].id
        ),
    ]

    db.session.add_all(species)
    db.session.commit()

print("Archives seeded")