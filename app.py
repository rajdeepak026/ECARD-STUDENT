from flask import Flask
from application.database import db
app = None

def creaate_app():
    app = Flask(__name__)
    app.debug = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecard.sqlite3"
    db.init_app(app)
    app.app_context().push() #runtime error, bring everything under context of flask application
    return app

app = creaate_app()
from application.controllers import *
# from application.models import * #indreect connection using controllers.py

if __name__=="__main__":
    app.run()


#ok
