from . import db, login_manager
from flask_login import UserMixin




class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    postal_address = db.Column(db.String(200), nullable=True)
    date_of_birth = db.Column(db.Date, nullable=True)
    marital_status = db.Column(db.String(50), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)  # Ajout de l'attribut is_admin
















    def set_password(self, password):
        self.password = password

    def check_password(self, password):
        return self.password == password

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Association(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False)