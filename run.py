#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""
import os
from onportrait import app

@app.cli.command()
def createdb():
    """
    initi database and migration information
    """
    SQLALCHEMY_DATABASE_URI = app.config['SQLALCHEMY_DATABASE_URI']

    if SQLALCHEMY_DATABASE_URI.startswith('sqlite:///'):
        path = os.path.dirname(os.path.realpath
                               (SQLALCHEMY_DATABASE_URI.replace(
                                   'sqlite:///', '')))
        if not os.path.exists(path):
            os.makedirs(path)

    db.create_all(app=app)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
