from app import app
from db import db  
db.init_app(app)  

def create():
    return app


if __name__ == "__main__":
    app.run(debug=True)