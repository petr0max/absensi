from absen import app, db
from absen.models import User, Sakit


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Sakit': Sakit}
