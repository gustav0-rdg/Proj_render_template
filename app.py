from flask import Flask, render_template
import random

app = Flask(__name__)

# Listas de nomes para alterar no html

nomes_lista = ["Godo", "Alex", "Ivo"]

# Aqui irá todas minhas rotas

@app.route("/")
def pagina_inicial():
    nome = random.choice(nomes_lista)
    return render_template('index.html')

# Fazer o app rodar
app.run(debug=True, host="0.0.0.0", port=8080)