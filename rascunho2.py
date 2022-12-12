class Conta:

    def __init__(self, conta, saldo):
        self.conta=conta
        self.saldo=saldo

    def depositar(self,valor):
        while(1):
            if valor == 0:
                print("INFORME OUTRO VALOR DIFERENTE DE ZERO")
                inicioDep()
            else:
                self.saldo += valor
                print(f'DINHEIRO DEPOSITADO FOI: R${valor}')
                print(f'SEU SALDO ATUAL É: R${self.saldo}')
                menu()


    def sacar(self, valor):
       while(1):
        if self.saldo < valor:
           print('SALDO INSUFICIENTE, TROQUE O VALOR')
           inicioSac()
        if valor == 0:
           print('VALOR INFORMADO FOI ZERO, INFORME OUTRO VALOR')
           inicioSac()
        else:
           self.saldo-=valor
           print(f'SAQUE APOVADO, VALOR DO SAQUE FOI DE: R${valor}\nSALDO RESTANTE DE R${self.saldo}')
           print(f'SEU SALDO ATUAL É: R${self.saldo}')
           menu()

def menu():
    while(1):
        try:
            x=float(input("------------------\n ( 1 ) DEPOSITAR \n ( 2 ) SACAR \n"))
            if x == 1:
                inicioDep()
            elif x==2:
                inicioSac()
            else:
                print('ESCOLHA SOMEMNTE (1) OU (2)')
        except ValueError:
                print('INFORME SOMENTE NÚMEROS, ESCOLHA (1) OU (2)')

mov=Conta('joao',0)
def inicioDep():
    while(1):
        try:
            x = (float(input("INFORME O VALOR DO DEPOSITO\n")))
            mov.depositar(x)
        except ValueError:
            print("INFORME SOMENTE NÚMEROS")

def inicioSac():
    mov.sacar(float(input('INFORME O VALOR DO SAQUE\n')))
    print(f'Seu Saldo é {mov.saldo}')
menu()



