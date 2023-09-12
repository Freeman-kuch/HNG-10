from flask import Flask
from flask_restful import Api
from resource.endpoints import bio, stage_2
from dotenv import load_dotenv
import os
from db import db

load_dotenv()

app = Flask(__name__)
print(os.getenv("DATABASE_URL"))
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)
db.init_app(app)
with app.app_context():
    db.create_all()



api.add_resource(bio, "/api")
api.add_resource(stage_2, "/api/<int:user_id>/")


if __name__ == "__main__":
    app.run(debug=True)


