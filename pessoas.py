'''
criado a clsse Pessoas
'''

class Pessoas:

#criando atrubuto da classe (terrestre para todas as pessoas)
    especie='terrestre'

    '''
construtor , self parametro de alta referencia,


CRIANDO OS ATRIBUTOS DO OBJETO
    '''

    def __init__(self, nome , idade, peso):
        self.setNome(nome)
        self.setIdade(idade)
        self.setPeso(peso)

    '''
    
    CRIANDO OS MÉTODOS DA CLASSE
    set,  método onde vai introduzir o valor no atributo nome, idade e peso, então são três métodos
    '''
    def setNome(self,nome):
        self.nome=nome
    def setIdade(self,idade):
        self.idade=idade
    def setPeso(self, peso):
        self.peso = peso
    '''
    get, retorno o atributo da classe
    '''
    def getNome(self):
        return self.nome
    def getIdade(self):
        return self.idade
    def getPeso(self):
        return self.peso


'''
CRIANDO OS OBJETOS DA CLASSE

OBJETOS PESSOAS

'''
pessoa1 = Pessoas("joão",43,102)
pessoa2 =Pessoas('maria', 47, 90)

'''
RETORNO ATRVÉS DA FUNÇÃO GET , O RETORNO DO OBJETO
'''

# função if __name__==__main__ é usada para ser executada somente quando a classe e executada dire   tamente
# se ela for chamada por outra classe o que estiver dentro do if não é executado
if  __name__ == "__main__":
    print('foi executado pelo __name__ == "__main__" está sendo executado diretamente o arquivo')
    print(f' Nome:{pessoa1.getNome()},Idade:{pessoa1.getIdade()},Peso:{pessoa1.getPeso()}')
    print(f' Nome:{pessoa2.getNome()},Idade:{pessoa2.getIdade()},Peso:{pessoa2.getPeso()}')
    s=Pessoas.especie
    print(s)
# ao contario do __name__=="__main__" , nesse caso a variavel recebe o nome do arquivo .py que nesse caso é pessoas
#então quando o aquivo é chamado diretamente a variavel __name__ recebe o valor "__main__" , quando um arquivo é chamado por outro
# a variavel __name__ recebe o nome do arquivo sem o .py
if  __name__ == "pessoas":
    print('foi executado pelo __name__ == "pessoas, está sendo executada por outro arquivo .py')
    print(f' Nome:{pessoa1.getNome()},Idade:{pessoa1.getIdade()},Peso:{pessoa1.getPeso()}')
    print(f' Nome:{pessoa2.getNome()},Idade:{pessoa2.getIdade()},Peso:{pessoa2.getPeso()}')
    s=Pessoas.especie
    print(s)

