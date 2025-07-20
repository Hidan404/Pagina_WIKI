import os

# Estrutura de diretórios e arquivos
estrutura = {
    "wiki_project": [
        "run.py",
        "requirements.txt",
        "README.md",
        "instance/config.py",
        "app/__init__.py",
        "app/models.py",
        "app/routes/__init__.py",
        "app/routes/main.py",
        "app/templates/base.html",
        "app/templates/home.html",
        "app/templates/all_wikis.html",
        "app/templates/wiki_detail.html",
        "app/static/styles.css"
    ]
}

def criar_estrutura(base, arquivos):
    for arquivo in arquivos:
        caminho_completo = os.path.join(base, arquivo)
        diretorio = os.path.dirname(caminho_completo)
        
        # Cria os diretórios se não existirem
        os.makedirs(diretorio, exist_ok=True)

        # Cria arquivos vazios se ainda não existirem
        if not os.path.exists(caminho_completo):
            with open(caminho_completo, 'w') as f:
                # Conteúdo básico para alguns arquivos comuns
                if arquivo.endswith('README.md'):
                    f.write("# Projeto Wiki\n")
                elif arquivo.endswith('requirements.txt'):
                    f.write("# flask\n")
                elif arquivo.endswith('config.py'):
                    f.write("DEBUG = True\nSECRET_KEY = 'sua_chave_secreta'\n")
                elif arquivo.endswith('__init__.py'):
                    f.write("# Inicialização de pacote\n")
                elif arquivo.endswith('.html'):
                    f.write(f"<!-- {os.path.basename(arquivo)} -->\n")
                elif arquivo.endswith('.py'):
                    f.write(f"# {os.path.basename(arquivo)}\n")
                elif arquivo.endswith('.css'):
                    f.write("/* Estilos da Wiki */\n")
            print(f"Criado: {caminho_completo}")
        else:
            print(f"Já existe: {caminho_completo}")

if __name__ == "__main__":
    for base, arquivos in estrutura.items():
        criar_estrutura(base, arquivos)
