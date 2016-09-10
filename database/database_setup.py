import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, Text, Numeric, ForeignKey

def connect (user='myapp', password='dbpass', host='localhost', port=15432, db='myapp'):
    # The url of our database hosted on the development Vagrant machine
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    
    # The connection objection
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # Binds the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta

con, meta = connect('developer', 'dbpass', 'localhost', 15432, 'market')

businesses = Table('businesses', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('address', String),
    Column('phone', String),
    Column('email', String),
    Column('website', String),
)

products = Table('products', meta,
    Column('id', Integer, primary_key=True),
    Column('business', Integer, ForeignKey("businesses.id"), nullable=False),
    Column('price', Numeric, nullable=False),
    Column('description', Text, nullable=False),
    Column('popularity', Integer),
)

users = Table('users', meta,
    Column('id', Integer, primary_key=True),
    Column('display_name', String, nullable=False),
    Column('password', String, nullable=False),
    Column('first_name', String, nullable=False),
    Column('last_name', String, nullable=False),
    Column('email', String, nullable=False),
)

reviews = Table('reviews', meta,
    Column('id', Integer, primary_key=True),
    Column('user', Integer, ForeignKey("users.id"), nullable=False),
    Column('product', Integer, ForeignKey("products.id"), nullable=False),
    Column('score', Integer, nullable=False),
    Column('details', Text),
)

meta.create_all(con)