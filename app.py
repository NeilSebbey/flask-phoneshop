import os

from flask import Flask
from extensions import pdb

# pdb instead of db

# create and configure the app
app = Flask(__name__)

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://mtu:mtu2021kerry@phone-shop-db-1.cmeabezboyem.us-east-1.rds.amazonaws.com:5432/phoneshop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "somethingunique"

pdb.init_app(app)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass


# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'


import db

db.init_app(app)

import auth

app.register_blueprint(auth.bp)

import main

app.register_blueprint(main.bp)

import admin

app.register_blueprint(admin.bp)

import inventory

app.register_blueprint(inventory.bp)

if __name__ == "__main__":
    app.run(debug=True)
