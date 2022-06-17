# models.py 

from app import db





class Test(db.Model):
    """"""
    __tablename__ = "test"

    id = db.Column(db.Integer, primary_key=True)
    Placa = db.Column(db.String)
    SubTotal = db.Column(db.Integer)
    

class Almacen(db.Model):
    """"""
    __tablename__ = "almacen"

    id = db.Column(db.Integer, primary_key=True)
    Producto = db.Column(db.String)
    Categoria = db.Column(db.String)
    Puntos = db.Column(db.Integer)
    Stock = db.Column(db.Integer)