from flask import Flask
from flask_jwt_extended import JWTManager
from db import db
from routes import api

app = Flask(__name__)

# KONEK KE MYSQL XAMPP
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@host.docker.internal:3306/appdb"
app.config["JWT_SECRET_KEY"] = "secret123"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
