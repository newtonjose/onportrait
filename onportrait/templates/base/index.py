from onportrait import app
from flask import render_template

@app.route('/')
@app.route('/upload')
def index():
    return render_template("index.html")