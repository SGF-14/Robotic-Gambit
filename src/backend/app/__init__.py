# __init__.py
from flask import Flask
from flask_cors import CORS
from .api import api_blueprint

from .match import initialize_matches
from .ComputerVision import setup_camera
from .FrameManagement import Squareupdate

def create_app():
    app = Flask(__name__)

    CORS(app)
    app.register_blueprint(api_blueprint)
    initialize_matches()
    Squareupdate()
    # setup_camera()
    # if setup_camera() is None:
    #     print("Camera setup failed. Camera features will not be available.")

    return app
