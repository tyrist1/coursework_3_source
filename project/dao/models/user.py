from project.dao.models.base import BaseMixin
from project.setup_db import db


class User(BaseMixin, db.Model):
    __tablename__ = "users"


    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    favorite_genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"))
    genre = db.relationship("Genre")

    def __repr__(self):
        return f"<User '{self.email.title()}'>" # почему .title
