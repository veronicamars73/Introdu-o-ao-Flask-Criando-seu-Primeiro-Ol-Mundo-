# Primeiro precisamos importar a Classe Flask da biblioteca Flask que instalamos
from flask import Flask

# Agora criaremos um objeto da classe Flask
app = Flask(__name__)

"""
Agora definiremos uma rota com o @app.route() o parâmetro dentro dos parênteses
representam um endereço do nosso domínio.
Quando usamos somente '/' nos parênteses estamos especificando a rota principal
do nosso site, ou seja só estamos buscando a página referente ao domínio do site
"""
@app.route('/')
def ola_mundo():
    return 'Olá Mundo!'

"""
Agora definiremos uma segunda rota com o @app.route() o parâmetro dentro dos
parênteses representam um endereço do nosso domínio. Nesse caso, nossa rota
será dominio.com.br/lisandra
"""
@app.route('/lisandra')
def ola_lisandra():
    return '<h1>Olá Lisandra!</h1>'

"""
Agora determinaremos que desejamos executar nosso app, para isso usamos o app.run()
poderíamos somente escrever isso no final do nosso programa, mas fazemos um teste
antes esse teste verifica se nossa variável __name__ é igual a '__main__' quando
um arquivo.py é executado por sozinho como um programa, __name__ é definido
como '__main__' logo se executarmos o nosso programa iremos executar o app.run()
"""
if __name__ == "__main__":
    app.run()
