from libs.API.brapi import brApi
from libs.database.dbAPI import Conexao
from flask import Flask, render_template, redirect, url_for, session, request, send_from_directory, abort
from flask_session import Session
from libs.funcs.pdfAPI import gerar_relatorio_valores
from libs.funcs.dataTime import data_hoje

app = Flask(__name__, template_folder="../frontend/templates")

app.static_folder = '../frontend/src'
app.static_url_path = '/static'

app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    pass

@app.route('/registro', methods=['POST'])
def registro():
    pass

@app.route('/logout', methods=['POST'])
def logout():
    pass

@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    pass

@app.route('/download')
def download():
    if request.method == 'POST':
        pass
    else:
        return abort(404)    

@app.route('/download/<filename>')
def download_file(filename):
    user = session.get('user')
    
    if request.method == 'POST':
        userPag = request.form.get('user')
        file = request.form.get('file')
            
        return send_from_directory(directory='../arquivos', path=filename + ".pdf")
    else:
        return abort(404)

if __name__ == "__main__":
    # gerar_relatorio_valores('teste', [["Receita", "Produto A", 10, 2, "Receitas", "01/08/2024"], ["Despesa", "Serviço B", 20, 1, "Despesas", "02/08/2024"], ["Receita", "Produto C", 30, 3, "Receitas", "03/08/2024"]], 1000.0, 'Bernardo', data_hoje())
    app.run(debug=True, port=8000)