from flask import Flask, Blueprint
from onportrait.index import index


def create_app(config):
    # Set up app, database and login manager before importing models
    # and controllers

    app = Flask(__name__, static_folder="./static/dist",
                template_folder="./onportrait/static")

    app.config.from_object(config)

    # Register Blueprints
    app.register_blueprint(index)

    return app
