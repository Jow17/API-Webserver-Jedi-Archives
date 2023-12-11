from setup import app
from blueprints.cli_bp import db_commands
from blueprints.jedi_bp import jedi_bp
from blueprints.planets_bp import planets_bp
from blueprints.species_bp import species_bp

app.register_blueprint(db_commands)
app.register_blueprint(jedi_bp)
app.register_blueprint(planets_bp)
app.register_blueprint(species_bp)

print(app.url_map)