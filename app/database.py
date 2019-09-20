from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import Base

def create_db():
	engine = create_engine('sqlite:///sqlite3.db') 
	engine.connect()
	print(engine)
	Base.metadata.create_all(engine)
	Session = sessionmaker(bind=engine)
	
	return Session()
