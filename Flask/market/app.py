from flask import Flask
from market.ext import configuration, create_db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
    app.config['SECRET_KEY'] = '55551cc547d71ce68cb6631a'
    configuration.init_app(app)
    configuration.load_extensions(app)
    return app
