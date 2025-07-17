from flask import Flask, render_template
import vercel_wsgi

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

handler = vercel_wsgi.handle(app)
