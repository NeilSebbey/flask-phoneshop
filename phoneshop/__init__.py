import os

from flask import Flask
from .extensions import pdb
# pdb instead of db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',

    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mtu:mtu2021kerry@phone-shop-db-1.cmeabezboyem.us-east-1.rds.amazonaws.com:5432/phoneshop'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "somethingunique"

    pdb.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import main
    app.register_blueprint(main.bp)

    from . import admin
    app.register_blueprint(admin.bp)

    from . import inventory
    app.register_blueprint(inventory.bp)

    return app
