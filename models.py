from flask_sqlalchemy import SQLAlchemy

GENERIC_IMAGE = 'https://img.freepik.com/free-photo/chubby-domestic-cat-leaning-brown-puppy-lying-white-surface_181624-45927.jpg?w=996&t=st=1666818817~exp=1666819417~hmac=555565f2180e20134c5ff00d5003b9cf94decb51072f4652b0ab036f3fe73831'

db = SQLAlchemy()


class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        return self.photo_url or GENERIC_IMAGE


def connect_db(app):
    db.app = app
    db.init_app(app)