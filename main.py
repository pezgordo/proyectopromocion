from app import app
from db_setup import init_db, db_session
from forms import AlmacenForm, PlacaSearchForm
from flask import flash, render_template, request, redirect
from models import Test, Almacen
from tables import Resultaputa, Results



init_db()


@app.route('/', methods=['GET', 'POST'])
def index():
    search = PlacaSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)


@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search_string:

        qry = db_session.query(Test).filter(Test.Placa.contains(search_string))
        results = qry.all()
        
        
    else:
        qry = db_session.query(Test)
        results = qry.all()





    if not results:
        flash('No results found!')
        return redirect('/')



    else:
        # display results
        table = Results(results)
        table.border = True

        return render_template('results.html', table=table)


@app.route('/ver_almacen')

def ver_almacen():
    results = []
    qry = db_session.query(Almacen)
    results = qry.all()
    table = Resultaputa(results)
    table.border = True

    return render_template('ver_almacen.html', table=table)




@app.route('/ingreso_almacen', methods=['Get', 'Post'])
def ingreso_almacen():
    """
    Ingresa nuevo producto
    """
    form = AlmacenForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the album
        almacen = Almacen()
        guardar_cambios(almacen, form, new=True)
        flash('Album created successfully!')
        return redirect('/')


    return render_template('ingreso_almacen.html', form=form)

def guardar_cambios(almacen, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    


    
    
    qry = db_session.query(Almacen)
    upval = qry.all()
    
    aQty = int(form.Stock.data)
    upVal = Almacen.query.filter_by(Producto = form.Producto.data).first()
    newUnits= upVal.Stock
    upVal.Stock = newUnits+aQty


    almacen.Producto = form.Producto.data 
    almacen.Puntos = form.Puntos.data
    almacen.Stock = newUnits + aQty
    #almacen.Stock = int(form.Stock.data) + nuevasudidades
    almacen.Categoria = form.Categoria.data
    
    

    if new:
        # Add the new album to the database
        db_session.update(almacen)

    # commit the data to the database
    db_session.commit()




if __name__ == '__main__':
    app.run()