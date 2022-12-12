# FUNÇÃO RECURSIVA DE PYTHON

def fatorial(numero):
    if numero==0 or numero==1:
        return 1
    else:
        return numero * fatorial(numero-1)
x=int(input('Digite um numero inteiro \n'))
res=fatorial(x)
print('O fatorial de %d é %d' % (x,res))