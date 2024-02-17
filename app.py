from flask import Flask, render_template, request
host = 'localhost'
port = 8080

app = Flask(__name__)


frutas = ['banana', 'maçã', 'uva', 'abacaxi']
registros = []
alunos = {'João': 8.5, 'Maria': 7.2, 'Pedro': 9.0, 'Ana': 6.8, 'Carlos': 8.9}
nomes = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get("nome"):
            nomes.append(request.form.get("nome"))
            
    if request.method == 'POST':
        if request.form.get("nome_aluno") and request.form.get("nota_aluno"):
            registros.append({"aluno":request.form.get("nome_aluno"), "nota":request.form.get("nota_aluno")})
    
    return render_template('index.html', 
                           frutas=frutas, 
                           alunos=alunos, 
                           nomes=nomes,
                           registros=registros)


app.run(host=host, port=port) 