from flask import Flask, render_template, jsonify #Importa biblioteca
import pygsheets
import os


credenciais = pygsheets.authorize(service_file=os.getcwd()+"/flask.json")


app = Flask(__name__) #Declarar o objeto Flask

@app.route("/index_1", methods=['GET']) ##Criar uma rota de acesso
def index_1():#associa uma função a esta rota
    return render_template('index_1.html') #retornma o resultado desta rota

@app.route("/index_2", methods=['GET']) ##Criar uma rota de acesso
def index_2():#associa uma função a esta rota
    return render_template('index_2.html') #retornma o resultado desta rota

@app.route("/meu_request", methods=['POST']) 
def meu_request():
    arquivo = credenciais.open_by_url("https://docs.google.com/spreadsheets/d/1hZZ2D-BwWlPvqshEnbuDsIZh7HcEfgkbVKcFK1ZQoS0/")
    aba = arquivo.worksheet_by_title("base_de_dados")
    celula_A1 = aba.get_row(1)[0]
 
    return jsonify(retorno=celula_A1)

if __name__ == '__main__':
    app.run(debug=True)