from flask_table import Table, Col 

class Results(Table):
    id = Col('id')
    Placa = Col('Placa')
    SubTotal = Col('SubTotal')

class Resultaputa(Table):
    id = Col('id', show=False)
    Producto = Col('Producto')
    Categoria = Col('Categoria')
    Puntos = Col('Puntos')
    Stock = Col('Stock')