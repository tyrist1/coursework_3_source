from flask import request
from flask_restx import abort, Namespace, Resource, reqparse

from project.exceptions import ItemNotFound
from project.services import UsersService
from project.setup_db import db

from project.tools.security import auth_required


users_ns = Namespace("users")
parser = reqparse.RequestParser()
parser.add_argument('page', type=int)


@users_ns.route("/")
class DirectorsView(Resource):
    @users_ns.expect(parser)
    @auth_required
    @users_ns.response(200, "OK")
    def get(self):
        """Get all users"""
        page = parser.parse_arg().get("page")
        if page:
            return UsersService(db.session).get_limit_users(page)
        else:
            return UsersService(db.session).get_all_users()


@users_ns.route("/<int:user_id>")
class UserView(Resource):
    @auth_required
    @users_ns.response(200, "OK")
    @users_ns.response(404, "User not found")
    def get(self, user_id: int):
        """Get director by id"""
        try:
            return UsersService(db.session).get_item_by_id(user_id)
        except ItemNotFound:
            abort(404, message="User not found")


    def patch(self, user_id: int):
        """частичное изменение"""
        req_json = request.json
        if not req_json:
            abort(400, message="Bad request")
        if not req_json('id'):
            req_json['id'] = user_id
        try:
            return UsersService(db.session).update(req_json)
        except ItemNotFound:
            abort(404, message="User not found")

class UserPatchView(Resource):
    @auth_required
    @users_ns.response(200, "OK")
    @users_ns.response(404, "User not found")
    def put(self, user_id: int):
        """частичное изменение"""
        req_json = request.json
        if not req_json:
            abort(400, message="Bad request")
        if not req_json('password'):
            req_json['password'] = 'password'
        try:
            return UsersService(db.session).update(req_json)
        except ItemNotFound:
            abort(404, message="User not found") #### есть ошибка