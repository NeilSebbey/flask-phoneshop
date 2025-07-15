import psycopg2
import click
import os
from flask import current_app, g
from sqlalchemy.testing import db

DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_NAME = os.getenv('DATABASE_NAME')


def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            host=DATABASE_HOST,
            user=DATABASE_USERNAME,
            password=DATABASE_PASSWORD,
            port=DATABASE_PORT,
            dbname=DATABASE_NAME
        )
    return g.db


def close_db(e=None):
    db = g.pop('db', None)


if db is not None:
    db.close()


def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.execute(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


@click.command('check-db')
def check_db_command():
    """Clear the existing data and create new tables."""
    db = get_db()
    cur = db.cursor()
    cur.execute("select * from user")
    users = cur.fetchall()
    print(users)


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(check_db_command)
