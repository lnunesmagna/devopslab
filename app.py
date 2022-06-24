from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Grupo 3 - MBA FIAP - Arquitetura de Soluções - Versão da api=GCP"

if __name__ == '__main__':
    #app.run()
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)