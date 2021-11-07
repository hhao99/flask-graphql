from flask import render_template
from app import app

@app.route('/')
def home():
    user = {'username': 'Eric'}
    return render_template('index.html',title='Flask GraphQL',user=user)