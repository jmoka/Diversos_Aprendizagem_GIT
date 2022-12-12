from numpy import *

elemento=(1,2)
indice= 2

nome=array([1,4,5],dtype=int)
print('sem mod')
print(nome)
print(nome[:-1])
print(nome)
print(nome, end='-')
print(elemento, end='-')
for n in nome:
    print(n, end='-')
print(elemento, end='@ \n')

matriz = array([['rita','rafaela','liko'],['suely','joly','junior'],['tatiana','milton','victor']],dtype=str)
matriz[1][2]='tereza'
print(matriz[1][2])
print(matriz)
def x():
    for linha in matriz:
        print('inicio da linha')
        for elemento in linha:
            elemento[1][2]='Brasil'
        return matriz[1][2]
print(x)



