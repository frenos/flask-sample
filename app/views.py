from flask import render_template, url_for
from app import app
from app import db, models


@app.route('/')
@app.route('/index')
def index():
    users = models.User.query.all()
    return render_template('index.html', title='hello', content=users)

@app.route('/create')
def create_user():
    new_user = models.User(nickname='a User')
    db.session.add(new_user)
    db.session.commit()
    return render_template('index.html', title='hello', content=[])