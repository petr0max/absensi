from flask import Flask, render_template
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config

# hash password module
from flask_bcrypt import Bcrypt

# Login Manager
from flask_login import LoginManager


mail = Mail()
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

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

    # Attach route for view and error

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .hadir import hadir as hadir_blueprint
    app.register_blueprint(hadir_blueprint, url_prefix='/absen')

    return app
