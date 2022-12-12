# CONFERINDO SE UM NÚMERO É PAR OU IMPAR
# DENTRO DE UMA ESTRUTURA FOR
# SERÁ CRIDO UM FOR ONDE A VARIAVEL NUMERO IRÁ PERCORRER UMA LISTA DO TIPO RANGER  QUE VAI DE 1 A 11
# 11 É OCULTO , ENTÃO A LISTA VAI DE 1 A 10 DE PASSO DE 1 A 1
# SERÁ IMPRESSO OS ITENS DA LISTA COM INFORMAÇÃO SE É PAR OU IMPAR
# ESTRUTURA FOR COM IF

soma_pares=0
conta_pares=0
soma_impar=0
conta_impar=0

print('INFORME OS PARAMETROS PARA O CÁLCULO')
inicio=eval(input('Informe um Número Inteiro INICIAL \n'))
fim=eval(input('Informe um Número Inteiro FINAL \n'))
for numero in range(inicio,fim,1):
      if numero%2==0:
            soma_pares = soma_pares + numero
            conta_pares += 1
      elif numero%2==1:
            soma_impar = soma_impar + numero
            conta_impar += 1
      else:
            continue # termina o if
print(f'Soma de pares é {soma_pares} dividido pela quantidade de números pares {conta_pares} a média de números pares é igual a {soma_pares/conta_pares}')
print(f'Soma de impares é {soma_impar} dividido pela quantidade de números impares {conta_impar} a média de números impares é igual a  {soma_impar / conta_impar}')








