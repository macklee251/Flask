from flask import Flask, render_template
host = 'localhost'
port = 8080

app = Flask(__name__)


frutas = ['banana', 'maçã', 'uva', 'abacaxi']
alunos = {'João': 8.5, 'Maria': 7.2, 'Pedro': 9.0, 'Ana': 6.8, 'Carlos': 8.9}
@app.route('/')
def index():
    return render_template('index.html', frutas=frutas, alunos=alunos)


app.run(host=host, port=port) 