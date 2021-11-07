from flask import render_template, flash, redirect, url_for, request, g, current_app
from app.main import bp

@bp.route('/')
def home():
    
    return render_template('index.html')