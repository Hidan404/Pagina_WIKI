from App import app
from flask import render_template, redirect, url_for

@app.route('/')
def home():
    return render_template('base.html')

@app.route("/home", methods=['GET'])
def home_page():
    return render_template('home.html')

@app.route("/wikis", methods=['GET'])
def wikis_page():
    return render_template('wikis.html')
