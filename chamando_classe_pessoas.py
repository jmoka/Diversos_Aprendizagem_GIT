
from pessoas import Pessoas

class pessoaFisica(Pessoas):
    def __init__(self, cpf, titulo,  nome, idade, peso):
        super().__init__(nome, idade, peso)
        self.cpf=cpf
        self.titulo=titulo
        '''
        set
        '''
    def setCpf(self,cpf):
        self.cpf = cpf

    def setTitulo(self, titulo):
        self.titulo = titulo

        '''
        get
        '''

    def getCpf(self):
       return self.cpf

    def getTitulo(self):
       return self.titulo

pf=pessoaFisica(123,456,'big', 43,99)


print(f' informação da chamada>>>.. cpf:{pf.getCpf()},cpf:{pf.getTitulo()}, nome:{pf.getNome()},idade:{pf.getIdade()}')
