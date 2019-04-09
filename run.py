from onportrait import create_app
from onportrait.index import index

app = create_app('config.DevelopmentConfig')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
