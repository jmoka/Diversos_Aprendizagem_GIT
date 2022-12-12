from datetime import date
class Pessoa:
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade

    # método de classe
    @classmethod
    def apartirAnoNascimento(cls,nome,ano):
        return cls(nome,date.today().year-ano)




    # método estático