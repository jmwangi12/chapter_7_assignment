from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    """shop URL"""
    return render_template('index.html', title='shop Page')

@app.route('/register')
def register():
    """register URL"""
    return render_template('register.html', title='registration Page')

@app.route('/login')
def login():
    """login URL"""
    return render_template('login.html', title='login Page')