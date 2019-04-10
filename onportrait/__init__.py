from flask import Flask
from onportrait.app import index_blueprint
from onportrait.app import upload_blueprint

app = Flask(__name__, static_folder='./public', template_folder='./static')

# register the blueprints
app.register_blueprint(index_blueprint)
app.register_blueprint(upload_blueprint)
