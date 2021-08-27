from flask import Flask, render_template
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config

# hash password module
from flask_bcrypt import Bcrypt

# Login Manager
from flask_login import LoginManager, current_user

# Flask Admin
from flask_admin import Admin, AdminIndexView, expose


mail = Mail()
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


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


admin = Admin(name='Admin Dashboard',
              template_mode='bootstrap4', index_view=AdminView())

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # config email
    mail.init_app(app)

    # config database
    db.init_app(app)

    # config hash password
    bcrypt.init_app(app)

    # Login Manager
    login_manager.init_app(app)

    # Flask Admin
    admin.init_app(app)

    # Attach route for view and error

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .hadir import hadir as hadir_blueprint
    app.register_blueprint(hadir_blueprint, url_prefix='/absen')

    from .profil import profil as profil_blueprint
    app.register_blueprint(profil_blueprint, url_prefix='/profile')

    from .admin import admins as admin_blueprint
    app.register_blueprint(admin_blueprint)

    return app
