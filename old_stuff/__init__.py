'''from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, Integer, String

# declaration of the base class

# declaration of a Mixin table to ease model development
class Base(object):
	
	@declared_attr
	def __tablename__(cls):
		return cls.__name__.lower()

	id =  Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)
'''
