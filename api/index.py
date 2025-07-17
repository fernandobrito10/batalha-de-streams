from flask import Flask, render_template
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__, template_folder="../templates")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/jogo')
def jogo():
    return render_template('jogo.html')

def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)
