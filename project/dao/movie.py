from sqlalchemy.orm.scoping import scoped_session

from project.dao.models import Movie


class MovieDAO:
    def __init__(self,  session: scoped_session):
        self._db__db_session =  session

    def get_by_id(self, pk):
        return self._db_session.query(Movie).filter(Movie.id == pk).one_or_none()

    def get_all(self):
        return self._db__db_session.query(Movie).all()
    
    def get_by_director_id(self, val):
        return self._db_session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_genre_id(self, val):
        return self._db_session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_year(self, val):
        return self._db_session.query(Movie).filter(Movie.year == val).all()

    def create(self, movie_d):
        ent = Movie(**movie_d)
        self._db_session.add(ent)
        self._db_session.commit()
        return ent

    def delete(self, rid):
        movie = self.get_one(rid)
        self._db_session.delete(movie)
        self._db_session.commit()

    def update(self, movie_d):
        obj = self.get_by_id(movie_d.get('id'))
        if obj:
            if movie_d.get('title'):
                obj.title = movie_d.get('title')
            if movie_d.get('description'):
                obj.description = movie_d.get('description')
            if movie_d.get('trailer'):
                obj.trailer = movie_d.get('trailer')
            if movie_d.get('year'):
                obj.year = movie_d.get('year')
            if movie_d.get('rating'):
                obj.rating = movie_d.get('rating')
            if movie_d.get('genre_id'):
                obj.genre_id = movie_d.get('genre_id')
            if movie_d.get('director_id'):
                obj.director_id = movie_d.get('director_id')


            self._db_session.add(movie_d)
            self._db_session.commit()
            return obj
        return "фильм не обновлялся"