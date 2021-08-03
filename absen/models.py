from . import db, bcrypt
from flask_login import UserMixin
from flask import current_app
from time import time
from . import login_manager
import jwt


class Permission:
    READ = 1
    UPDATE = 2
    DELETE = 3
    CREATE = 4
    FOLLOW = 5
    COMMENT = 6
    WRITE = 7
    MODERATE = 10
    ADMIN = 16
    OWNER = 23


# For models database
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, perm):
        return self.permissions & perm == perm

    @staticmethod
    def insert_roles():
        roles = {
            'User': [Permission.FOLLOW, Permission.COMMENT. Permission.WRITE],
            'Moderator': [Permission.FOLLOW, Permission.COMMENT,
                          Permission.WRITE, , Permission.MODERATE],
            'Admin' : [Permission.FOLLOW, Permission.COMMENT,
                       Permission.]
        }
    def __repr__(self):
        return f"<Role {self.name}>"


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    username= db.Column(db.String(64), unique=True, index=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128), unique=True, nullable=False)
    confirmed = db.Column(db.Boolean, default=False)


    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password, rounds=10)

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


    def generate_confirmation_token(self, expiration=3600):
        secret_key = current_app.config['SECRET_KEY']
        token = jwt.encode({'confirm': self.id, 'exp': time() + expiration},
                           secret_key,
                           algorithm='HS256')
        return token

    def confirm(self, token):
        secret_key = current_app.config['SECRET_KEY']
        try:
            data = jwt.decode(token, secret_key, algorithms=['HS256'])
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def generate_reset_token(self, expiration=3600):
        secret_key = current_app.config['SECRET_KEY']

        return jwt.encode({'reset_password': self.id, 'exp': time() + expiration},
                           secret_key,
                           algorithm='HS256')


    @staticmethod
    def verify_reset_password_token(token, new_password):
        secret_key = current_app.config['SECRET_KEY']
        try:
            id = jwt.decode(token, secret_key,
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


    # Database representation
    def __repr__(self):
        return f"<User {self.email}"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
