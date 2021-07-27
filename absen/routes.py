from absen import app
from flask import render_template, url_for, session, redirect, flash
from absen.forms import NameForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', title='Beranda', form=form,
                           name=session.get('name'))

@app.route('/home')
def home():
    return '<h1>You are the home page</h1>'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post {post_id}"

@app.route('/coba/<path:subpath>')
def show_subpath(subpath):
    return f"Path {escape(subpath)}"

@app.route('/json')
def json():
    return jsonify({'key': 'value', 'listkey': [1, 2, 3, 4]})
