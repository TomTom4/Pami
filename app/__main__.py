#from app.database import create_db
#import app.model

#session = create_db()

from app.view import ViewApp
from app.controller import Controller

controller = Controller()
ViewApp(controller=controller).run()

