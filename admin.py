from flask import Blueprint, render_template, request, redirect, url_for, flash

from auth import login_required
from extensions import pdb
from models import Phone

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
@login_required
def index():
    phones = Phone.query.all()
    return render_template('admin/index.html', phones=phones)


@bp.route('/add/', methods=['GET', 'POST'])
@login_required
def insert_phone():
    if request.method == "POST":
        phone = Phone(
            model=request.form.get('model'),
            brand=request.form.get('brand'),
            storage=request.form.get('storage'),
            colour=request.form.get('colour'),
            network=request.form.get('network'),
            os=request.form.get('os'),
            condition=request.form.get('condition'),
            price=request.form.get('price'),
            s3img=request.form.get('s3img'),
        )
        pdb.session.add(phone)
        pdb.session.commit()
        flash("Phone added successfully")
        return redirect(url_for('admin.index'))

    return render_template('admin/add_phone.html')


@bp.route('/update/', methods=['POST'])
@login_required
def update():
    if request.method == "POST":
        my_data = Phone.query.get(request.form.get('id'))

        my_data.model = request.form['model']
        my_data.brand = request.form['brand']
        my_data.storage = request.form['storage']
        my_data.colour = request.form['colour']
        my_data.network = request.form['network']
        my_data.os = request.form['os']
        my_data.condition = request.form['condition']
        my_data.price = request.form['price']
        my_data.s3img = request.form['s3img']

        pdb.session.commit()
        flash("Phone is updated")
        return redirect(url_for('admin.index'))


@bp.route('/delete/<id>/', methods=['GET', 'POST'])
@login_required
def delete(id):
    my_data = Phone.query.get(id)
    pdb.session.delete(my_data)
    pdb.session.commit()
    flash("Phone is deleted")
    return redirect(url_for('admin.index'))
