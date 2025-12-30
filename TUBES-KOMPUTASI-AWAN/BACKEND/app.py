from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "secret123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)
jwt = JWTManager(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    role = db.Column(db.String(20))

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    status = db.Column(db.String(20))
    user_id = db.Column(db.Integer)

def init_db():
    with app.app_context():
        db.create_all()
        if not User.query.first():
            db.session.add(User(username="admin", password="admin", role="manager"))
            db.session.add(User(username="user", password="user", role="user"))
            db.session.commit()

init_db()

@app.route("/")
def home():
    return {"msg": "Backend OK"}

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()
    if not user or user.password != data["password"]:
        return {"msg": "Login gagal"}, 401
    token = create_access_token(identity={"id": user.id, "role": user.role})
    return {"token": token}

@app.route("/api/request", methods=["POST"])
@jwt_required()
def create_request():
    user = get_jwt_identity()
    data = request.json
    message = data["message"]
    r = Request(title=data["title"], status="pending", user_id=user["id"])
    db.session.add(r)
    db.session.commit()
    return {"msg": "Request dibuat"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
