from flask import request, jsonify
from flask_jwt_extended import jwt_required, create_access_token
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from sqlalchemy.exc import IntegrityError
from database import db, UserModel
from schemas import UserSchema

blp = Blueprint("user", __name__, description="Operations on user")


@blp.route("/user")
class UserList(MethodView):

    @jwt_required()
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, user_data):
        user = UserModel(username=user_data["username"],
                         password=pbkdf2_sha256.hash(user_data["password"]))
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(404, message="User already exists")
        return user


@blp.route("/user/<string:uid>")
class User(MethodView):
    @jwt_required()
    @blp.response(200, UserSchema)
    def get(self, uid: str):
        user = UserModel.query.get_or_404(uid)
        return user

    @jwt_required()
    @blp.response(200, UserSchema)
    def delete(self, uid: str):
        user = UserModel.query.get_or_404(uid)
        db.session.delete(user)
        db.session.commit()
        return user


@blp.route("/login")
class Login(MethodView):

    def post(self):
        name = request.json.get("username")
        password = request.json.get("password")

        user = db.session.query(UserModel).filter(UserModel.username == name).first()

        if user and pbkdf2_sha256.verify(password, user.password):
            access_token = create_access_token(identity=user.id)
            user.access_token = access_token
            return jsonify({'access_token': access_token})
        else:
            abort(400, "Invalid login or password")