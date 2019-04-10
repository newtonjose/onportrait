from onportrait import app
import logging

logging.getLogger('onportrait').setLevel(logging.DEBUG)

app.config.from_object('config.DevelopmentConfig')

#app = app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
