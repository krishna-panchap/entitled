from flask import Flask
import os
from config import appConfig
from waitress import serve

config = {}
config = appConfig

def create_app(config_class=config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.inference import bp as inference_bp
    app.register_blueprint(inference_bp, url_prefix="/inference")


    if (os.environ.get("FLASK_ENV") == "development"):
        return app
    elif (os.environ.get("FLASK_ENV") == "production"):
        serve(app, host='0.0.0.0', port=5002)