from flask_restx import abort, Namespace, Resource

from project.exceptions import ItemNotFound
from project.services import MovieService
from project.setup_db import db

movies_ns = Namespace("movies")


@movies_ns.route("/")
class MoviesView(Resource):
    @movies_ns.response(200, "OK")
    def get(self):
        """Get all movies"""
        return MovieService(db.session).get_all_movies()


@movies_ns.route("/<int:movies_id>")
class GenreView(Resource):
    @movies_ns.response(200, "OK")
    @movies_ns.response(404, "Movies not found")
    def get(self, movies_id: int):
        """Get movie by id"""
        try:
            return MovieService(db.session).get_item_by_id(movies_id)
        except ItemNotFound:
            abort(404, message="Movie not found")
