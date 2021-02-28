from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sam'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Mantorville!'
        },
        {
            'author': {'username': 'Hannah'},
            'body': 'Money Heist was such a cool show!'
        }
    ]
    return render_template('index.html', title='Poolside', user=user, posts=posts)
