# -*- encoding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='./public', template_folder='./static')

#Configuration of application, see configuration.py, choose one and uncomment.
#app.config.from_object('configuration.ProductionConfig')
app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

#app.config.from_object('configuration.TestingConfig')

db = SQLAlchemy(app) #flask-sqlalchemy
#db.create_all(app=app)
#lm = LoginManager()
#lm.setup_app(app)
#lm.login_view = 'login'

from onportrait import api, models

# register the blueprints
app.register_blueprint(api.index_blueprint)
app.register_blueprint(api.upload_blueprint)
app.register_blueprint(api.add_portrait_blueprint)
app.register_blueprint(api.get_portrait_image_blueprint)
app.register_blueprint(api.get_portrait_blueprint)
