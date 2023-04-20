from flask import Blueprint, render_template, request, redirect, url_for, flash

from auth import login_required
from extensions import pdb
from models import Phone, Brands

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
@login_required
def index():
    phones = Phone.query.all()
    brands = Brands.query.all()
    return render_template('admin/index.html', phones=phones, brands=brands)


"""
#    Title:  app.py, lines 29-62
#    Author: Parwiz Forogh
#    Site owner/sponsor:  github.com
#    Date: Dec 6, 2022, 1:19 GMT
#    Code version:  6beef35b50fca17d2ad2f84e7de042c7c396c712
#    Availability:  https://github.com/parwiz123/flaskaws/blob/main/app.py
(Accessed 20 March 2023)
#    Modified:  Code refactored (Identifiers renamed) 
"""
@bp.route('/add_phone/', methods=['GET', 'POST'])
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


@bp.route('/add_brand/', methods=['GET', 'POST'])
@login_required
def insert_brand():
    if request.method == "POST":
        brand = Brands(
            brand=request.form.get('brand'),
            description=request.form.get('description'),
            s3_logo_url=request.form.get('s3_logo_url'),
            flask_href=request.form.get('flask_href'),
        )
        pdb.session.add(brand)
        pdb.session.commit()
        flash("Brand added successfully")
        return redirect(url_for('admin.index'))

    return render_template('admin/add_brand.html')


@bp.route('/update_phone/', methods=['POST'])
@login_required
def update_phone():
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


@bp.route('/update_brand/', methods=['POST'])
@login_required
def update_brand():
    if request.method == "POST":
        my_data = Brands.query.get(request.form.get('id'))

        my_data.brand = request.form['brand']
        my_data.description = request.form['description']
        my_data.s3_logo_url = request.form['s3_logo_url']
        my_data.flask_href = request.form['flask_href']

        pdb.session.commit()
        flash("Brand is updated")
        return redirect(url_for('admin.index'))


@bp.route('/delete_phone/<id>/', methods=['GET', 'POST'])
@login_required
def delete_phone(id):
    my_data = Phone.query.get(id)
    pdb.session.delete(my_data)
    pdb.session.commit()
    flash("Phone is deleted")
    return redirect(url_for('admin.index'))


@bp.route('/delete_brand/<id>/', methods=['GET', 'POST'])
@login_required
def delete_brand(id):
    my_data = Brands.query.get(id)
    pdb.session.delete(my_data)
    pdb.session.commit()
    flash("Brand is deleted")
    return redirect(url_for('admin.index'))


# end of refactored code
