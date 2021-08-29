from .. import db
import datetime


class Title(db.Model):
    __tablename__ = 'titles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_title = db.Column(db.String(64), index=True, unique=True)
    choices = db.relationship('Choice', backref='title', lazy='dynamic')

    def __repr__(self):
        return f"{self.name_title.title()}"


class Choice(db.Model):
    __tablename__ = 'choices'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_choice = db.Column(db.String(64), index=True)

    timehours = db.relationship('TimeHour', backref='choice', lazy='dynamic')
    #users = db.relationship('User', backref='choice', lazy='dynamic')
    choice_id = db.Column(db.Integer, db.ForeignKey('titles.id'))

    def __repr__(self):
        return f"{self.name_choice}"


class TimeHour(db.Model):
    __tablename__ = 'timehours'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time_start = db.Column(db.Time())
    time_end = db.Column(db.Time())
    choice_id = db.Column(db.Integer, db.ForeignKey('choices.id'))
