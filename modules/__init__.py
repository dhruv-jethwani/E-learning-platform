from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os # <-- Import os to handle file paths

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ABCD IJKL'

    # Define the path to your SQLite database file
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(app.instance_path, "database.db")}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Ensure the instance folder exists for SQLite to create the db file
    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)

    # --- THIS IS THE CHANGE YOU NEED TO MAKE ---
    # Import your models here AFTER db.init_app(app)
    # This makes Flask-SQLAlchemy aware of the models so db.create_all() can find them.
    from . import models # <--- UNCOMMENT OR ADD THIS LINE

    # It's common to create tables *after* db.init_app(app) and after models are defined.
    # A simple way for development:
    with app.app_context():
        db.create_all() # This creates all tables defined in your SQLAlchemy models

    from .views import views
    from .auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app