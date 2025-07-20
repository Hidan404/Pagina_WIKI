# main.py
from flask import Blueprint, render_template, request, redirect, url_for
from app.models import db, Wiki, Comment

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    wikis = Wiki.query.order_by(Wiki.created_at.desc()).limit(5).all()
    return render_template('home.html', wikis=wikis)

@bp.route('/wikis')
def all_wikis():
    search = request.args.get('q', '')
    if search:
        wikis = Wiki.query.filter(Wiki.title.contains(search)).all()
    else:
        wikis = Wiki.query.all()
    return render_template('all_wikis.html', wikis=wikis, search=search)

@bp.route('/wiki/<int:wiki_id>', methods=['GET', 'POST'])
def wiki_detail(wiki_id):
    wiki = Wiki.query.get_or_404(wiki_id)
    if request.method == 'POST':
        author = request.form['author']
        text = request.form['text']
        comment = Comment(author=author, text=text, wiki=wiki)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.wiki_detail', wiki_id=wiki_id))
    return render_template('wiki_detail.html', wiki=wiki)
