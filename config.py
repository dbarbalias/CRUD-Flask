import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key-123'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:////' + os.path.join(base_dir, 'app/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
