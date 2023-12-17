from flask import Blueprint
from setup import db, bcrypt
from models.jedi import Jedi
from models.planet import Planet
from models.species import Species
from models.status import Status
from models.rank import Rank
from sqlalchemy import text

db_commands = Blueprint('db', __name__)

@db_commands.cli.command("create")
def db_create():
    db.drop_all()
    db.create_all()
    print("Created tables")

# Adds data to the database table columns
@db_commands.cli.command("seed") 
def db_seed():
    statuses = [
        Status(
            title = "Alive",
        ),
        Status(
            title = "Deceased",
        ),
        Status(
            title = "Unknown",
        )
    ]

    db.session.add_all(statuses)
    db.session.commit()

    ranks = [
        Rank(
            title = "Councilmember",
        ),
        Rank(
            title = "Master",
        ),
        Rank(
            title = "Knight",
        ),
    ]

    db.session.add_all(ranks)
    db.session.commit()

    jedi = [
        Jedi(
            username="Grandmaster01",
            jedi_name="Yoda",
            access_code=bcrypt.generate_password_hash("sizemattersnot").decode("utf8"),
            rank_title = "Councilmember",
            species_name = "Unknown",
            current_location = "Coruscant",
            status_title = "Alive",
        ),
        Jedi(
            username="Uncle_Ben",
            jedi_name="Obi-wan_Kenobi",
            access_code=bcrypt.generate_password_hash("highground24").decode("utf8"),
            rank_title = "Master",
            species_name = "Human",
            current_location = "Kamino",
            status_title = "Alive"
        ),
        Jedi(
            username="Chosen_1",
            jedi_name="Anakin_Skywalker",
            access_code=bcrypt.generate_password_hash("Idontlikesand").decode("utf8"),
            rank_title= "Knight",
            species_name= "Human",
            current_location = "Tatooine",
            status_title = "Alive"
        ),
        Jedi(
            username = "Quigonnagym",
            jedi_name = "Qui-gon_Jinn",
            access_code = bcrypt.generate_password_hash("Midichlorians123").decode("utf8"),
            rank_title = "Master",
            species_name = "Human",
            current_location = "Jedi Temple",
            status_title = "Deceased"
        )
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
            jedi_id = jedi[0].id,
        ),
        Planet(
            planet_name="Kamino",
            sector="Abrion",
            population="1 billion",
            allegiance="Independent",
            jedi_id = jedi[1].id,
        ),
    ]

    db.session.add_all(planets)
    db.session.commit()

    species = [
        Species(
            species_name = "Human",
            designation = "Sentient",
            lifespan = "80 years",
            jedi_id = jedi[1].id
        ),
        Species(
            species_name = "Unknown",
            designation = "Sentient",
            lifespan = "80 years",
            jedi_id = jedi[0].id
        ),
    ]
    
    db.session.add_all(species)
    db.session.commit()


print("Archives seeded")