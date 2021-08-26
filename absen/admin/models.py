from .. import db, admin, bcrypt
from flask import request, url_for, redirect
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask_admin import AdminIndexView, expose
from ..models import User
from ..profil.models import Profile
from ..hadir.models import Permit, Absen


class UserView(ModelView):
    column_exclude_list = []
    column_display_pk = True
    can_create = True
    can_edit = True
    can_delete = True
    can_export = True

    def on_model_change(self, form, model, is_created):
        model.password = bcrypt.generate_password_hash(
            model.password, rounds=10)


class AdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated \
            and current_user.is_administrator()

    def inaccesible_callback(self, name, **kwargs):
        return redirect(url_for('main.index', next=request.url))

    @expose('/')
    def index(self):
        if not current_user.is_authenticated \
                and current_user.is_administrator():
            return redirect(url_for('main.index'))
        return super(AdminView, self).index()


admin.add_view(UserView(User, db.session))
admin.add_view(ModelView(Profile, db.session))
admin.add_view(ModelView(Absen, db.session))
admin.add_view(ModelView(Permit, db.session))
