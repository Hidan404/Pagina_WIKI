from app import app
from App import db

# Ativa o contexto da aplicação
with app.app_context():
    db.create_all()
    print("Banco de dados criado com sucesso!")

