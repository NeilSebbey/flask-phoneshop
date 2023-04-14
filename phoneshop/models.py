from .extensions import pdb


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
    s3img = pdb.Column(pdb.String(100))
