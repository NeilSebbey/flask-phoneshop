from extensions import pdb


class Phone(pdb.Model):
    id = pdb.Column(pdb.Integer, primary_key=True)
    model = pdb.Column(pdb.String(30), nullable=False)
    brand = pdb.Column(pdb.String(20), nullable=False)
    storage = pdb.Column(pdb.String(10), nullable=False)
    colour = pdb.Column(pdb.String(10), nullable=False)
    network = pdb.Column(pdb.String(10), nullable=False)
    os = pdb.Column(pdb.String(10), nullable=False)
    condition = pdb.Column(pdb.String(20), nullable=False)
    price = pdb.Column(pdb.Float)
    staticimg = pdb.Column(pdb.String(100))


class Brands(pdb.Model):
    id = pdb.Column(pdb.Integer, primary_key=True)
    brand = pdb.Column(pdb.String(20), nullable=False)
    description = pdb.Column(pdb.String(500), nullable=False)
    static_logo_url = pdb.Column(pdb.String(100))
    flask_href = pdb.Column(pdb.String(100))
