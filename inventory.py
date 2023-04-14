from flask import Blueprint, render_template

from extensions import pdb
from models import Phone

bp = Blueprint('inventory', __name__, url_prefix='/inventory')


@bp.route('/')
def index():
    return render_template('inventory/index.html')


@bp.route('/brands/apple')
def apple_phones():
    apple = Phone.query.filter_by(brand='Apple')
    return render_template('inventory/brands/apple.html', apple=apple)


@bp.route('/brands/samsung')
def samsung_phones():
    samsung = Phone.query.filter_by(brand='Samsung')
    return render_template('inventory/brands/samsung.html', samsung=samsung)
