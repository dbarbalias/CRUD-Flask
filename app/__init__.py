from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config())
db = SQLAlchemy(app)

from app import modules, routes #need to bring in the modules b4 creating db; at bottom to avoid circular reference
