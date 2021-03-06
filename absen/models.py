from . import db, bcrypt, admin
from flask_login import UserMixin, AnonymousUserMixin
from flask import current_app
from time import time
from . import login_manager
import datetime
import jwt


class Permission:
    FOLLOW = 1
    COMMENT = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16
    OWNER = 32


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

    @staticmethod
    def insert_roles():
        roles = {
            'User': [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE],
            'Moderator': [Permission.FOLLOW, Permission.COMMENT,
                          Permission.WRITE, Permission.MODERATE],
            'Admin' : [Permission.FOLLOW, Permission.COMMENT,
                       Permission.WRITE, Permission.MODERATE,
                       Permission.ADMIN],
            'Owner' : [Permission.FOLLOW, Permission.COMMENT,
                       Permission.WRITE, Permission.MODERATE,
                       Permission.ADMIN, Permission.OWNER],
        }
        default_role = 'User'
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()


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


    def __repr__(self):
        return f"<Role {self.name}>"


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username= db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128), unique=True)
    confirmed = db.Column(db.Boolean, default=False)
    member_since = db.Column(db.Date(), default=datetime.date.today())
    last_seen = db.Column(db.DateTime(), default=datetime.datetime.now())
    
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    profiles = db.relationship('Profile', backref='user', uselist=False)
    permits = db.relationship('Permit', backref='user', lazy='dynamic')
    absens = db.relationship('Absen', backref='user', lazy='dynamic')
    sicks = db.relationship('Sick', backref='user', lazy='dynamic')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['ABSEN_ADMIN']:
                self.role = Role.query.filter_by(name='Admin').first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    @property
    def pass_hash(self):
        raise AttributeError('password is not readable attribute')

    @pass_hash.setter
    def pass_hash(self, pass_hash):
        self.password = bcrypt.generate_password_hash(pass_hash, rounds=10)

    def verify_password(self, pass_hash):
        return bcrypt.check_password_hash(self.password, pass_hash)

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

        return jwt.encode({'reset': self.id, 'exp': time() + expiration},
                           secret_key,
                           algorithm='HS256')


    @staticmethod
    def reset_password(token, new_password):
        secret_key = current_app.config['SECRET_KEY']
        try:
            data = jwt.decode(token, secret_key,
                            algorithms=['HS256'])['reset']
        except:
            return False
        user = User.query.get(data)
        if user is None:
            return False
        user.password = bcrypt.generate_password_hash(new_password, rounds=10)
        db.session.add(user)
        return True


    # Database representation
    def __repr__(self):
        return f"{self.username.title()}"

    def can(self, perm):
        return self.role is not None and self.role.has_permission(perm)

    def is_moderate(self):
        return self.can(Permission.MODERATE)

    def is_administrator(self):
        return self.can(Permission.ADMIN)

    def is_owner(self):
        return self.can(Permission.OWNER)


    def ping(self):
        self.last_seen = datetime.datetime.now()
        db.session.add(self)
        db.session.commit()


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
