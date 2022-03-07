from project.dao import DirectorDAO
from project.exceptions import ItemNotFound
from project.schemas.director import DirectorSchema
from project.services.base import BaseService
from project.services import DirectorsService
from project.tools.security import auth_required

directors_ns = Namespace("directors")
parser = reqparse.ReuestParser()
parser.add_argument('page', type=int)


@directors_ns.route("/")
class DirectorsService(Resource):
    def get_item_by_id(self, pk):
        genre = GenreDAO(self._db_session).get_by_id(pk)
        if not genre:
            raise ItemNotFound
        return GenreSchema().dump(genre)

    def get_all_genres(self):
        genres = GenreDAO(self._db_session).get_all()
        return GenreSchema(many=True).dump(genres)
