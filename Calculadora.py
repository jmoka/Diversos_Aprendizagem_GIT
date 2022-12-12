  """
funções de somar de subtrair, multiplicar e subtrar

"""
def soma (a,b):
    """
    funções de somar primeiro numero mais o segundo numero
    """
    return a+b
def subtracao (a,b):
    return a-b
def mutiplicacao(a,b):
    return a*b
def divisao (a,b):
    return a/b
numero1=eval(input('Inform o Primeiro Número:\n'))
numero2=eval(input('Inform o Segundo Número:\n'))
numero3=eval(input('''ESCOLHA UMA DAS OPÇÕES\n1-soma\n2-subtração\n3-mutiplicação\n4-divisão\n'''))
if numero3==1:
   print('Sua Soma foi:', soma(numero1,numero2))
elif numero3==2:
   print('Sua Subtração foi:',subtracao(numero1,numero2))
elif numero3 == 3:
   print('Sua Mutiplicação foi:',mutiplicacao(numero1,numero2))
elif numero3 ==4:
   print('sua Divisão foi:',divisao(numero1,numero2))
else:
   numero3()
















