from onportrait.app import app
from onportrait.app import index_blueprint
from onportrait.app import upload_blueprint
from onportrait.app import add_portrait_blueprint
import logging

logging.getLogger('onportrait').setLevel(logging.DEBUG)

app.config.from_object('config.DevelopmentConfig')

# register the blueprints
app.register_blueprint(index_blueprint)
app.register_blueprint(upload_blueprint)
app.register_blueprint(add_portrait_blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
