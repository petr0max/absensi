from flask import Flask, render_template
from markupsafe import escape
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 400

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

from absen import routes

if __name__ == '__main__':
    app.run(debug=True)
