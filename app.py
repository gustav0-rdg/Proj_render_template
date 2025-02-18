from flask import Flask, render_template,request,redirect
import random
import os
import mysql.connector
from data import listas_configuracao as listas
from data import conexao
0

app = Flask(__name__)
x = 0
# Listas de nomes para alterar no html

@app.route("/", methods=["GET"])
def pagina_inicial():
    cor_fundo = random.choice(listas.lista_cores)
    # Selecionando a imagem que eu quero
    global imagem_lista
    # Entrando na pasta das imagens
    caminho_imagens = os.path.join(app.root_path, 'static', 'img')
    # selecionando todas e fazendo uma lista
    imagem_lista = [f'img/{arquivo}' for arquivo in os.listdir(caminho_imagens)]
    # Selecionando um aleatorio das listas para alterar sempre que entrar no site
    nome = random.choice(listas.nomes_lista)
    curiosidade = random.choice(listas.curiosidades)
    imagem = random.choice(imagem_lista)
    return render_template('index.html', nome = nome, curiosidade = curiosidade, imagem = imagem, cor_fundo = cor_fundo)

@app.route("/sobre")
def sobre():
    cor_fundo = random.choice(listas.lista_cores)
    return render_template('sobre.html', cor_fundo = cor_fundo)

@app.route("/cadastro", methods=["GET"])
def cadastro():
    return render_template('cadastro.html', frases_html = listas.curiosidades)

@app.route("/post/cadastrarfrase", methods=["POST"])
def post_cadastrarFrase():
    frase = request.form.get("frase")
    listas.curiosidades.append(frase)
    return redirect ("/cadastro")

@app.route("/cadastroCores", methods=["GET"])
def cadastro_cores():
    return render_template('cadastro-cores.html', cores_html = listas.lista_cores, x = x)

@app.route("/post/cadastrarcores", methods=["POST"])
def post_cadastrarCor():
    cor = request.form.get("cor")
    listas.lista_cores.append(cor)
    return redirect ("/cadastroCores")

@app.route("/cadastroCores/delete/<indice_cor>")
def delete_cores(indice_cor):
    indice_cor = int(indice_cor)
    listas.lista_cores.pop(indice_cor)
    return redirect("/cadastroCores")


# Fazer o app rodar
app.run(debug=True, host="0.0.0.0", port=8080)
