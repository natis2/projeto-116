# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'

@app.route("/eu")
def home1():

    nome = "Natalia" # escreva seu nome
    idade = "14" # escreva sua idade

    return render_template('index.html' , name = nome , age = idade)

# defina a rota para a página do pai
@app.route("/pai")
def home2():

    nome = "Ronei" # escreva seu nome
    idade = "49" # escreva sua idade

    return render_template('pai.html' , nome = nome , idade = idade)

# defina a rota para a página da mãe
@app.route("/mae")
def home3():

    nome = "Monica" # escreva seu nome
    idade = "50" # escreva sua idade

    return render_template('mae.html' , nome = nome , idade = idade)


# defina a rota para a página do amigo


# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
