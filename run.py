import os
from absen import create_app, db
from absen.models import User, Role, Permission
from absen.hadir.models import Permit, Absen
from absen.profil.models import Profile
from flask_migrate import Migrate


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Permission=Permission,
                Permit=Permit, Profile=Profile, Absen=Absen)

@app.cli.command()
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == "__main__":
    app.run()
