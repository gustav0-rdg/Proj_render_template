from flask import Flask, render_template
import random
import os

app = Flask(__name__)

# Listas de nomes para alterar no html

nomes_lista = ["Godo", "Alex", "Ivo"]
curiosidades = ["Indivíduos com Síndrome de Down têm uma terceira cópia do cromossomo 21.", "A síndrome de Down é a causa genética mais comum de deficiência intelectual.", "O nome 'Síndrome de Down' vem de John Langdon Down, o médico que a descreveu em 1862.", "Cerca de 1 em cada 700 nascimentos tem um bebê com Síndrome de Down.", "Indivíduos com Síndrome de Down podem ter uma expectativa de vida de até 60 anos ou mais.", "A Síndrome de Down pode causar atrasos no desenvolvimento cognitivo e motor, mas cada pessoa é única em suas habilidades e limitações.", "A prevalência de Síndrome de Down não depende da raça ou etnia.", "Crianças com Síndrome de Down podem aprender a ler e escrever, embora com ritmos e métodos de ensino adaptados.", "A síndrome de Down é diagnosticada geralmente logo após o nascimento, com base em características físicas e testes genéticos.", "Indivíduos com Síndrome de Down têm maior risco de problemas cardíacos, mas muitos podem levar uma vida saudável com o acompanhamento médico adequado.","Existem diferentes tipos de Síndrome de Down, sendo a mais comum a trissomia 21, onde há uma cópia extra do cromossomo 21.", "A maioria das pessoas com Síndrome de Down tem uma estatura mais baixa que a média, mas isso pode variar.", "Crianças com Síndrome de Down podem se beneficiar de terapias precoces, como fisioterapia, fonoaudiologia e terapia ocupacional, para melhorar suas habilidades.", "A detecção precoce de Síndrome de Down pode ser feita por exames genéticos durante a gravidez, como o teste de amniocentese ou o teste de DNA fetal.", "Embora a maioria das pessoas com Síndrome de Down tenha algum grau de deficiência intelectual, muitos têm habilidades excepcionais em áreas como música, arte e esportes.", "A presença de um cromossomo extra no DNA é a única causa conhecida para a Síndrome de Down.", "O risco de uma mulher ter um filho com Síndrome de Down aumenta com a idade, especialmente após os 35 anos.", "Embora a Síndrome de Down traga desafios, muitos indivíduos têm carreiras, amizades e vidas independentes e plenas.", "A capacidade de comunicação de uma pessoa com Síndrome de Down pode ser melhorada com o uso de sinais, gestos e outras formas de linguagem alternativa.", "Estudos sugerem que a inclusão escolar de crianças com Síndrome de Down promove um ambiente mais positivo e inclusivo para todos os alunos."]
# Aqui irá todas minhas rotas
lista_cores = [
    "red","violet","#ababaa", "green"
]

@app.route("/")
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
# Fazer o app rodar
app.run(debug=True, host="0.0.0.0", port=8080)
