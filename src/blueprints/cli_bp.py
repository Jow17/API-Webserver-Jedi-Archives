from flask import Blueprint
from setup import db, bcrypt
from models.jedi import Jedi
from models.planet import Planet


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
            first_name="Obi-wan",
            last_name="Kenobi",
            access_code=bcrypt.generate_password_hash("highground24").decode("utf8"),
            rank = "Master",
            apprentice = "Anakin Skywalker",
            location = "Kamino",
            status = "Alive"
        ),
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
            jedi_assigned = "Obi-Wan Kenobi",
        ),    
        Planet(
            planet_name="Coruscant",
            sector="Corusant", 
            population="trillions",
            allegiance = "Republic",

        )
    ]
    db.session.add_all(planets)
    db.session.commit()





print("Database seeded")