'''importando flask'''
from flask import Flask, render_template, request, redirect, url_for, session
import calendar

app = Flask(__name__)
app.secret_key = 'chave_secreta'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        funcionarios = request.form['funcionarios'].split(',')
        session['funcionarios'] = [nome.strip() for nome in funcionarios]
        return redirect(url_for('ordem'))
    return render_template('index.html')

@app.route('/ordem', methods=['GET', 'POST'])
def ordem():
    if 'funcionarios' not in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        ordem = request.form.getlist('ordem')
        session['ordem'] = ordem
        return redirect(url_for('escala'))
    return render_template('ordem.html', funcionarios=session['funcionarios'])

@app.route('/escala', methods=['GET', 'POST'])
def escala():
    if 'ordem' not in session:
        return redirect(url_for('ordem'))
    escala = []
    if request.method == 'POST':
        data = request.form['data']
        dia, mes, ano = map(int, data.split('/'))
        if calendar.weekday(ano, mes, dia) == 5:  # Sábado
            indice_funcionario = len(session.get('escala', [])) % len(session['ordem'])
            session.setdefault('escala', []).append((data, session['ordem'][indice_funcionario]))
        return redirect(url_for('escala'))
    return render_template('escala.html', escala=session.get('escala', []))

if __name__ == '__main__':
    app.run(debug=True)
