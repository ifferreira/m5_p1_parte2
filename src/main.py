from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB, Query

db = TinyDB('caminhos.json')
app = Flask(__name__)


# rota raiz
@app.route('/')
def home():
    return render_template('index.html')

# rota novo
@app.route('/novo', methods=['POST'])
def novo():
    x = request.form['x']
    y = request.form['y']
    z = request.form['z']
    r = request.form['r']
    db.insert({'x': x, 'y': y, 'z': z, 'r': r})
    return redirect(url_for('index'))


# rota para atualizar conforme o id
@app.route('/atualizar/<int:id>')
def atualizar(id):
    caminho = db.get(doc_id=id)
    return render_template('atualizar.html', caminho=caminho)

# rota atualizar
@app.route('/atualizar', methods=['POST'])
def update():
    x = request.form['x']
    y = request.form['y']
    z = request.form['z']
    r = request.form['r']
    id_caminho = request.form['id']
    db.update({'x': x, 'y': y, 'z': z, 'r': r}, doc_ids=id_caminho)
    return redirect(url_for('index'))

# rota deletar
@app.route('/deletar', methods=['POST'])
def delete():
    x = request.form['x']
    db.remove(Query().x == x)
    return redirect(url_for('index'))

# rota para listar conforme o id
@app.route('/pegar_caminho/<int:id>')
def pegar_caminho(id):
    caminho = db.get(doc_id=[id])
    return render_template('listas_caminho.html', caminho=caminho)

# rota listar
@app.route('/listas_caminhos')
def index():
    caminhos = db.all()
    return render_template('listas_caminho.html', caminhos=caminhos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
