from flask import Flask
host = "localhost"
port = 8080

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!" 

app.run(host=host, port=port)