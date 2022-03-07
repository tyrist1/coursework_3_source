from flask import request
from flask_restx import abort, Namespace, Resource, reqparse

from project.exceptions import ItemNotFound
from project.services import UsersService
from project.setup_db import db

from project.tools.security import auth_required


auth_ns = Namespace("auth")
parser = reqparse.ReuestParser()
parser.add_argument('page', type=int)


@auth_ns.route("/")
class AuthView(Resource):
    def post(self):
        req_json = request.json
        if not req_json:
            abort(400, message="Bad request")
        try:
            user = UsersService(db.session).get_item_by_email(email=req_json.get("email"))
            tokens = login_user(request.json, user)
            return tokens, 200
        except ItemNotFound:
            abort(404, message="Error, ошибка автоматизации")



@auth_ns.route("/register")
class AuthRegisterView(Resource):
    def post(self):
        req_json = request.json
        if not req_json:
            abort(400, message="Bad request")
        return UsersService(db.session).create(req_json)
