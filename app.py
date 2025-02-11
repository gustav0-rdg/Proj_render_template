from flask import Flask, render_template,request,redirect
import random
import os

app = Flask(__name__)
x = 0
# Listas de nomes para alterar no html

nomes_lista = ["Godo", "Alex", "Ivo"]
curiosidades = ["Indivíduos com Síndrome de Down têm uma terceira cópia do cromossomo 21."]
# Aqui irá todas minhas rotas
lista_cores = [
    "red","violet","#ababaa", "green"
]

@app.route("/", methods=["GET"])
def pagina_inicial():
    cor_fundo = random.choice(lista_cores)
    # Selecionando a imagem que eu quero
    global imagem_lista
    # Entrando na pasta das imagens
    caminho_imagens = os.path.join(app.root_path, 'static', 'img')
    # selecionando todas e fazendo uma lista
    imagem_lista = [f'img/{arquivo}' for arquivo in os.listdir(caminho_imagens)]
    # Selecionando um aleatorio das listas para alterar sempre que entrar no site
    nome = random.choice(nomes_lista)
    curiosidade = random.choice(curiosidades)
    imagem = random.choice(imagem_lista)
    return render_template('index.html', nome = nome, curiosidade = curiosidade, imagem = imagem, cor_fundo = cor_fundo)

@app.route("/sobre")
def sobre():
    cor_fundo = random.choice(lista_cores)
    return render_template('sobre.html', cor_fundo = cor_fundo)

@app.route("/cadastro", methods=["GET"])
def cadastro():
    return render_template('cadastro.html', frases_html = curiosidades)

@app.route("/post/cadastrarfrase", methods=["POST"])
def post_cadastrarFrase():
    frase = request.form.get("frase")
    curiosidades.append(frase)
    return redirect ("/cadastro")

@app.route("/cadastroCores", methods=["GET"])
def cadastro_cores():
    return render_template('cadastro-cores.html', cores_html = lista_cores, x = x)

@app.route("/post/cadastrarcores", methods=["POST"])
def post_cadastrarCor():
    cor = request.form.get("cor")
    lista_cores.append(cor)
    return redirect ("/cadastroCores")

# Fazer o app rodar
app.run(debug=True, host="0.0.0.0", port=8080)
