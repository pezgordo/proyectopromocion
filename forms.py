from wtforms import Form, StringField, SelectField

class PlacaSearchForm(Form):

   
    search = StringField('')


class AlmacenForm(Form):

    categoria_types = [('Moda', 'Moda'),
                 ('Auto', 'Auto'),
                 ('Casa', 'Casa')
                ]

    Producto = StringField('Producto')
    Puntos = StringField('Puntos')
    Categoria = SelectField('Categoria', choices=categoria_types)
    Stock = StringField('Stock')
    