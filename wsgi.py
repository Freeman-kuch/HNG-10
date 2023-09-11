from app import app


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)