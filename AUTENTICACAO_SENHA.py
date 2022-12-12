class Autenticacao:
    def __init__(self, usuario, senha, usuario_db, senha_db):
        self.usuario = usuario
        self.senha = senha
        self.usuario_db = usuario_db
        self.senha_db = senha_db
def coleta():
    # COLETAR DADOS USUARIO
    # USUARIO
    usuario1 = input('INFORME O USUÁRIO: \n')
    # CONFERIR SENHA
    senha1 = input('INFORME SUA SENHA: \n')

    # INFORMAÇÃO DO BANCO DE DADOS
    usuario_db1 = 'jose'
    senha_db1 = '123'

    # FORMATAÇÃO
    formatacao = '{0} {1} {2} {3}'
    formato = formatacao.format(usuario1, senha1, usuario_db1, senha_db1)

    # INSTACIAÇÃO
    instancia = Autenticacao(usuario1, senha1, usuario_db1, senha_db1)

    # TESTE
    print('formato--------> ', formato)
    print('usuario--------->', instancia.usuario)
    print('senha----------->', instancia.senha)
    print('usuario_db------>', instancia.usuario_db)
    print('senha_db-------->', instancia.senha_db)

    while(1):
        if instancia.usuario ==instancia.usuario_db:
            print("USUÁRIO CORRETO")
            if instancia.senha==instancia.senha_db:
                print('SENHA CORRETA')
            else:
                print("INFORME OUTRA SENHA")
        else:
            print('INFORME OUTRO USUÁRIO')



if __name__=="__main__":
    coleta()

