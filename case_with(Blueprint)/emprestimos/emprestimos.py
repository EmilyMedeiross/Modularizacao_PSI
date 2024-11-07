from flask import Flask, render_template, url_for, request, Blueprint, redirect
from emprestimos.models import Emprestimo 
from users.models import User

bp = Blueprint('emprestimos', __name__, url_prefix='/emprestimos', template_folder='templates')

@bp.route('/')
def index():
    return render_template('emprestimos/index.html', emprestimos = Emprestimo.all())

@bp.route('/register', methods=['POST', 'GET'])
def register():

    if request.method == 'POST':
        user = request.form['user']
        titulo = titulo.form['titulo']
        data_emprestimo = request.form['data_emprestimo']
        

        emprestimo = Emprestimo(user,titulo, data_emprestimo)
        emprestimo.save()
        return redirect(url_for('emprestimos.index'))


    return render_template('emprestimos/register.html', users=User.all())