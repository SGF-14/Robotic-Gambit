from flask import Flask
from flask_cors import CORS
from .api import api_blueprint
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    app.register_blueprint(api_blueprint)
    return app
