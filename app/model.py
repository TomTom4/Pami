from app import Base
from sqlalchemy import Column, Integer, String


class User(Base):
	name = Column(String(50))
	password = Column(String(128))

	def __repr__(self):
		return f"<User: {self.name})"

class Mail(Base):

	subject = Column(String(128))
	message = Column(String(1024))

	def __repr__(self):
		return f"Mail: {self.subject}"
	
