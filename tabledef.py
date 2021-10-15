from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///tutorial.db', echo=True)
Base = declarative_base()
#i am agod
########################################################################
class User(Base):
    """"""
__tablename__ = "users"

id = Column(Integer, primary_key=True)
username = Column(String)
password = Column(String)

#----------------------------------------------------------------------
def __init__(self, username, password):
    """"""
self.username = username
self.password = password

# create tables
Base.metadata.create_all(engine)
bcrypt.hashpw(request.form['pass'], login_user['password']) == login_user['password'].encode('utf-8'):
