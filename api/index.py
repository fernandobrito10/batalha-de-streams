from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/jogo')
def jogo():
    return render_template('jogo.html')

if __name__ == "__main__":
    app.run(debug=True)