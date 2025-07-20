from App import app
from flask import render_template, redirect, url_for
from App.models import User, db, Comentario
 
@app.route('/')
def home():
    return render_template('base.html')

@app.route("/home", methods=['GET'])
def home_page():
    return render_template('home.html')

@app.route("/wikis", methods=['GET'])
def wikis_page():
    return render_template('wikis.html')

@app.route("/wiki_detalhes", methods=["GET"])
def all_wikis():
    return render_template('wiki_detalhes.html')


@app.route("/comentar", methods=["POST"])
def comentario():
    comentar = Comentario.query.order_by(Comentario.data_criacao.desc()).limit(5).all()
    return render_template('home.html', comentar=comentar)