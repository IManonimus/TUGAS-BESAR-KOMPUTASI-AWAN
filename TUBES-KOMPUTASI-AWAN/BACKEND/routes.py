from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User, Request
from db import db
from auth import generate_token

api = Blueprint("api", __name__)

@api.route("/", methods=["GET"])
def home():
    return {"message": "Backend aktif 🚀"}

@api.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()

    if not user or user.password != data["password"]:
        return {"msg": "Login gagal"}, 401

    return {
        "token": generate_token(user),
        "role": user.role
    }

@api.route("/request", methods=["POST"])
@jwt_required()
def create_request():
    user = get_jwt_identity()
    data = request.json

    req = Request(
        title=data["title"],
        description=data["description"],
        status="pending",
        user_id=user["id"]
    )
    db.session.add(req)
    db.session.commit()

    return {"msg": "Request berhasil dibuat"}

@api.route("/request", methods=["GET"])
@jwt_required()
def get_request():
    user = get_jwt_identity()

    if user["role"] == "manager":
        data = Request.query.all()
    else:
        data = Request.query.filter_by(user_id=user["id"]).all()

    return jsonify([
        {"id": r.id, "title": r.title, "status": r.status}
        for r in data
    ])
