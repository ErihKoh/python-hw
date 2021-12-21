from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from assistant_app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def loader_use(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), index=True, unique=True)
    email = db.Column(db.String(60), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Contact', backref='author', lazy='dynamic')

    def __repr__(self):
        return f"User: {self.username}"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    phone = db.Column(db.Integer())
    address = db.Column(db.String(140))
    email = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f" Name: {self.name}\n Phone: {self.phone}\n Email: {self.email}\n Address: {self.address}"
