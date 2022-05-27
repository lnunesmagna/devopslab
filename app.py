from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Grupo 3 - MBA FIAP - Arquitetura de Soluções"

if __name__ == '__main__':
    app.run()