import os
from flask import Flask
from extensions import pdb

# environmental variables for DB connection and secrets
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_NAME = os.getenv('DATABASE_NAME')
SECRET_KEY = os.getenv('SECRET_KEY')

# create and configure the app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ('postgresql://' + DATABASE_USERNAME + ':' + DATABASE_PASSWORD +
                                         '@' + DATABASE_HOST + ':' + DATABASE_PORT + '/' + DATABASE_NAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = SECRET_KEY

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
