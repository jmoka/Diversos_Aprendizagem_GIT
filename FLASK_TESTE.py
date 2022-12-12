from flask import Flask

app1 = Flask(__name__)

@app1.route('/ola', methods=['POST'])
def ola_post():
    return "Olá, GET"

@app1.route('/ola')
def ola_get(nome="mundo"):
    return "Olá, POST"

if __name__ == '__main__':
    app1.run()