"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """users."""

    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        return self.authenticated


class PlayedSong(db.Model):
    """Song."""

    __tablename__ = "PlayedSongs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("Users.id", ondelete="CASCADE"), nullable=False
    )
    song_name = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(400), nullable=False)
    addedAt = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(50), nullable=False)


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
