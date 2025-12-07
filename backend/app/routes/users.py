from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.utils.validators import validate_register_data, validate_login_data, validate_update_data

users_bp = Blueprint('users', __name__)


@users_bp.post("/register")
def register():
    data = request.json
    errors = validate_register_data(data)
    
    if errors:
        return jsonify({"message": ", ".join(errors)}), 400
    
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    nama = data.get("nama")
    
    result, status_code = UserService.register(username, password, email, nama)
    return jsonify(result), status_code


@users_bp.post("/login")
def login():
    data = request.json
    errors = validate_login_data(data)
    
    if errors:
        return jsonify({"message": ", ".join(errors)}), 400
    
    username = data.get("username")
    password = data.get("password")
    
    result, status_code = UserService.login(username, password)
    return jsonify(result), status_code


@users_bp.get("")
def get_users():
    result, status_code = UserService.get_all_users()
    return jsonify(result), status_code


@users_bp.put("/<int:user_id>")
def update_user(user_id):
    data = request.json
    errors = validate_update_data(data)
    
    if errors:
        return jsonify({"message": ", ".join(errors)}), 400
    
    username = data.get("username")
    email = data.get("email")
    nama = data.get("nama")
    
    result, status_code = UserService.update_user(user_id, username, email, nama)
    return jsonify(result), status_code


@users_bp.delete("/<int:user_id>")
def delete_user(user_id):
    result, status_code = UserService.delete_user(user_id)
    return jsonify(result), status_code

