from flask import render_template
from app import app

from app.users import users
from app.posts import posts

for user in users:
    user['posts'] = []
    for post in posts:
        if user['id'] == post['userId']:
            user['posts'].append(post)


@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/<int:id>')
def show_by_id(id):
    return render_template('index.html', users=list(filter(lambda item: item['id'] == id, users)))

@app.route('/city/<city>')
def users_by_city(city):
    return render_template('index.html', users=list(filter(lambda item: item['address']['city'] == city, users)))
