from flask import Flask
from flask_restful import Api
from resource.endpoints import bio


app = Flask(__name__)
api = Api(app)



api.add_resource(bio, "/", "/bio")



if __name__ == "__main__":
    app.run(debug=True)
