class Salario:
    def __init__(self,salario, comissao):
        self.salario=salario # atributos da classe
        self.comissao=comissao # atributos da classe

    def salario_anual(self):
        # recebe os parametros de salario total
        # Recebe os dois paramentros (slario,comissao)
        #
        return (self.salario*12)+self.comissao

class Empregados:
    # nesse momento houve a agregação quando passa como paramento salario1 que é uma estancia da classe Salario
    # nesse momento é passado para a classe empregado um parametro que coresponde a classe Salario
    def __init__(self, nome, idade, salario1):
        self.nome=nome
        self.idade=idade
        self.salario1 = salario1


    def salario_total(self):
        # self.salario1 passsa para salario anual os dois parametros da isntancia ou seja slario de valor 10000 e comissão de 700
        return self.salario1.salario_anual()


# chamada
salario1=Salario(10000,700) # estanciar a classe salário no objeto salario
emp=Empregados('jota',46,salario1)
print(emp.salario_total())