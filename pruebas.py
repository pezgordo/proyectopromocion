from hashlib import new
from pprint import pp
from app import app
from db_setup import init_db, db_session
from forms import AlmacenForm, PlacaSearchForm
from flask import flash, render_template, request, redirect
from models import Test, Almacen
from tables import Resultaputa, Results
from sqlalchemy import func, distinct


init_db()




####

#qry = db_session.query(Almacen).filter(Almacen.Stock.like('12%')).all()
#qry = db_session.query(func.count(Almacen.Stock)).group_by(Almacen.Stock).all()
#for i in qry:
   # print(i)
###



qry = db_session.query(Almacen)
#upval = qry.all()
    
aQty = 8
upVal2 = Almacen.query.first()
upVal = Almacen.query.filter_by(Producto = "hora").first()
newUnits= upVal.Stock
#upVal.Stock = newUnits+aQty

#print(upVal.Stock)
#print(upVal)
print(upVal)
print(newUnits)


