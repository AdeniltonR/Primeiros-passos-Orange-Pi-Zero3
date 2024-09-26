'''
 * NOME: Adenilton Ribeiro
 * DATA: 13/09/2024
 * PROJETO: Flask com Orange Pi Zero 3
 * VERSAO: 01
 * DESCRICAO: - feat: Criar página  de exemplo.
 * LINKS: 
'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():

    return render_template("homepage.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)