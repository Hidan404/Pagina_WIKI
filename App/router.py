from App import app
from flask import render_template, redirect, url_for

@app.route('/')
def home():
    return render_template('base.html')
