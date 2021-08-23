from .. import db, admin, bcrypt
from flask_admin.contrib.sqla import ModelView
from ..models import User
from ..profil.models import Profile
from ..hadir.models import CheckIn, CheckOut, Permit, Sick


class UserView(ModelView):
    column_exclude_list = []
    column_display_pk = True
    can_create = True
    can_edit = True
    can_delete = True
    can_export = False

    def on_model_change(self, form, model, is_created):
        model.password = bcrypt.generate_password_hash(
            model.password, rounds=10)


admin.add_view(UserView(User, db.session))
admin.add_view(ModelView(Profile, db.session))
admin.add_view(ModelView(CheckIn, db.session))
admin.add_view(ModelView(CheckOut, db.session))
admin.add_view(ModelView(Sick, db.session))
admin.add_view(ModelView(Permit, db.session))


def is_accessible(self):
    return current_user.is_administrator
