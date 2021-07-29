from absen import db
from flask_login import UserMixin
from . import login_manager
import bcrypt


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# For models database
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Role {self.name}>"


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    username= db.Column(db.String(64), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generater_password_hash(password).decode('utf-8')

    # Verify user
    def verify_password(self, password):
        return bcrypt.check_password_hash(password_hash, password)

    @property
    def is_authenticated(self):
        return self.authenticated

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    
    # Function get ID
    def get_id(self):
        return str(self.id)


    # Database representation
    def __repr__(self):
        return f"<User {self.email}"
