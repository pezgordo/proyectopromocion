import sqlalchemy as db

engine = db.create_engine('sqlite:///test.sqlite')
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('test', metadata, autoload=True, autoload_with=engine)

print(repr(metadata.tables['test']))