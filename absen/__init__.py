from flask import Flask, jsonify
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>hai</h1>'

@app.route('/home')
def home():
    return '<h1>You are the home page</h1>'

@app.route('/<name>')
def hello(name):
    return f"Hello, {name}"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post {post_id}"

@app.route('/coba/<path:subpath>')
def show_subpath(subpath):
    return f"Path {escape(subpath)}"

@app.route('/json')
def json():
    return jsonify({'key': 'value', 'listkey': [1, 2, 3, 4]})

if __name__ == '__main__':
    app.run(debug=True)
