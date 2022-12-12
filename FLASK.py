from flask import Flask

app = Flask(__name__)


@app.route('/') # pasta rais com informação com somente a barra
def raiz():
    return "Pasta Raiz."

@app.route('/pagina') # pasta ou rota com o nome pagina
def pagina():
    return "Pasta Pagina"

@app.route('/pagina/pagina2/') #pagina 2 ou rota 2
@app.route('/pagina/pagina2/<nome>') # paramentro nome
def pagina2(nome='___Pagina2'):
    return 'Pagina 2' + nome

#importante
@app.route('/pagina/pagina2/pagina3/')
def pagina3():
    pagina3='<h1>pagina3</h1>'
    link = '<p><a href="http://contabilidade.jotaempresas.com">Clique aqui!</a></p>'
    return pagina3 + link

@app.route('/pagina/pagina2/pagina3/pagina4')
@app.route('/pagina/pagina2/pagina3/pagina4/<nome>')
def pagina4(nome='usuario'):
    personalizar=f'<h1>__pagina4__, {nome}</h1>'
    instrucao='<p>Altere o nome <em>  endereço do Browser <em>\ e recarregue a pagina.</p>'
    return personalizar + instrucao


# vamos somar dois parametros
@app.route('/pagina/pagina2/pagina3/pagina4/pagina5/')
@app.route('/pagina/pagina2/pagina3/pagina4/pagina5/<numero1>/<numero2>')
def soma(numero1=0, numero2=0):
    calculo=float(numero1) + float(numero2)
    return str(calculo)


if __name__ == '__main__':
   app.run()