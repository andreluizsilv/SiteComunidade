from flask import Flask, render_template, url_for
from forms import FormCriarConta, FormLogin

app = Flask(__name__)

lista_usuarios = 'Lira', 'João', 'Alon', 'Alessandra', 'Amanda'

app.config['SECRET_KEY'] = '57533e07a7431b7bbeb5a063f8ae2eca'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route("/base")
def base():
    return render_template('base.html')

@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route("/login")
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)



if __name__ == '__main__':
    app.run(debug=True)