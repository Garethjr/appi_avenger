from flask import Flask
from routes.avengers import avenger_bp
from config.config import DATABASE_CONECTION_URI
from models.db import db
app = Flask(__name__)
app.register_blueprint(avenger_bp)

app.secret_key = "SECRET_KEY"
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    from models.avenger import Avenger
    db.drop_all()
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)