from flask import Flask
from flask_restful import Api
from resource.endpoints import bio, stage_2
from dotenv import load_dotenv
import os

load_dotenv()
def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQL_THINGY")
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    api = Api(app)



    api.add_resource(bio, "/api")
    api.add_resource(stage_2, "/api/<int:user_id>/")

    return app



