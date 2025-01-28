from flask import Flask, render_template
import random

app = Flask(__name__)

nomes_lista = ["Godo", "Alex", "Ivo"]
@app.route("/")
def pagina_inicial():
    nome = random.choice(nomes_lista)
    return render_template('index.html', nome = nome)

app.run(debug=True, host="0.0.0.0", port=8080)