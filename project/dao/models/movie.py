from project.dao.models.base import BaseMixin
from project.setup_db import db


class Movie(BaseMixin, db.Model):
    __tablename__ = 'movies'

    name = db.Column(db.String(100), unique=True, nullable=False)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255), nullable=False)
    trailer = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    genre = db.relationship("Genre")
    director = db.relationship("Director")

    def __repr__(self):
        return f"<Movie '{self.name.title()}'>"
