from flask import Flask

from config import Config
from models.database import db, migrate
from serial_number.views import serial_number


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db, compare_type=True)

app.register_blueprint(serial_number, url_prefix='/')
