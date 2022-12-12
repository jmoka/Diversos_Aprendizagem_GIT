'''
PILHAS, FILAS, TUPLAS e CONJUNTOS
'''

'''PILHAS'''
'''
AS PILHAS SÃO ESTRUTURAS MUTÁVEIS , NÃO HOMOGENIAS , LINEARES, DINAMICAS
POSSUEM SOMENTE UM LOCAL DE ENTRADA DE ELEMENTOS E O MESMO PARA SAIDA DE ELEMENTOS
O ULTIMO QUE ENTRA É O PRIMEIRO A SAIR
NAS PILHAS OS VALORES PODEM SER REPETIDOS E ALTERADOS
É REPRESENTADA [] IGUALMENTE UMA LISTA
'''
PILHA1=[0,9,'q','d']
print('=====================================')
print('PILHAS')
print('=====================================')
PILHA= []
# INSERINDO NUMERO 1 NA PILHA
PILHA.append(1)
print('iseruiu um itam na pilha')
print(PILHA)
PILHA.append(1)
print('iseruiu MAIS UM itam na pilha')
print(PILHA)
PILHA.append('e')
print('iseruiu STRING itam na pilha')
print(PILHA)
PILHA.append([1,2])
print('iseruiu LSITA itam na pilha')
print(PILHA)
PILHA.append((5,6))
print('iseruiu TUPLA itam na pilha')
print(PILHA)
PILHA.append({2,'i','f',8})
print('iseruiu CONJUNTO itam na pilha')
print(PILHA)

# RETIRAR UM ITEM DA PILHA
PILHA.pop()
print('RETIROU O ULTIMO ELEEMENTO QUEE NO CASO É, O CONJUNTO 2,i,'f',8')
print(PILHA)
PILHA.pop(4)
print('RETIROU X O ULTIMO ELEEMENTO QUEE NO CASO É, O CONJUNTO 2,i,'f',8')
print(PILHA)

# ALTERANDO O VALOR DE UM ITEM DA PHILHA PELO SEU INDICE
print('ALTERANDO O VALOR DO ELEMENTO DA PILHA')
PILHA[3]=2
print(PILHA)

print('UNINDO AS PILHAS')
PILHA1.extend(PILHA)
print(PILHA1)
print('ALTERANDO ITEM DE UMA PILHA UNIFICADA, ATRAVÉS DO INDICE')
PILHA1[5]=7
print(PILHA1)
print('INVERTENDO OS ITEM DE UMA PILHA')
PILHA1.reverse()
print(PILHA1)
print('REMOVENDO UM ITEM DA PILHA')
PILHA1.remove('e')
print(PILHA1)

print('INSERINDO USANDO O INSERT, TENDO QUE USAR 2 PARAMETROS UM ITEM DA PILHA')
PILHA1.insert(1,'E')
print(PILHA1)

print('INDEX RETORNA O INDICE DO ELEMENTO DA PILHA')
PILHA2=[1,'R','Y',7,7,7]
Z=PILHA2.index('R')
print(Z)

print('CÓPIA DA PILHA USANDO COPY')
PILHA1.copy()
print(PILHA1)

print('CONTA A QUANTIDADE VE VEZES QUE UM ELEMENTO DA PILHA SE REPETE')
V=PILHA2.count(7)
print(V)

print('CONTA A QUANTIDADE DE ELEMENTOS DA PILHA')
V= len(PILHA2)
print(V)


'''FILAS'''
'''
AS FILAS SÃO ESTRUTURAS MUTÁVEIS , NÃO HOMOGENIAS , LINEARES, DINAMICAS
POSSUEM SOMENTE UM LOCAL DE ENTRADA DE ELEMENTOS E UM SAIDA DE ELEMENTOS
O PRIMEIRO QUE ENTRA É O PRIMEIRO QUE SAI
NAS FILA OS VALORES PODEM SER REPETIDOS
É REPRESENTADA [] IGUALMENTE UMA LISTA E AS PILHAS
'''

print('=====================================')
print('PILHAS')
print('=====================================')

FILA=[]

print('INSERI UM VALOR NA FILA')
FILA.append(1)
print(FILA)
print('INSERI UM VALOR NA FILA')
FILA.append(2)
print(FILA)
print('INSERI UMA STRING NA FILA')
FILA.append('W')
print(FILA)
print('INSERI UMA OUTRA FILA')
FILA.append([1,2])
print(FILA)

'''
RETIRANDO UM VALOR DA FILA
'''
print('RETIRANDO UM VALOR DA FILA')
FILA.pop(2)
print(FILA)







'''
CONJUNTOS
''
Ingualmente uma lista os conjuntos são MUTÁVEIS  e seus elementos são NÃO HOMOGENIOS, 
ou seja pode ser d diversos tipos.
MESMO SENDO MUTAVEL SEUS ELEMENTOS NÃO PODEM SER ALTERADOS
E IGUALMENTE AS LISTAS NÃO POSSUEM INDICES, POR NÃO SEREM ORDENADOS
'''
print('=====================================')
print('CONJUNTOS')
print('=====================================')
a={6,7,8,9,0,'b'}
d={1,2,3,4,'a'}
d.pop()
print(d)
d.pop()
print(d)
d.pop()
print(d)
d.pop()
print(d)
d.pop()
print(d)

conjunto_a = {1, 2, 3}
conjunto_b = {4, 5, 6}
conjunto_c = {3, 4, 5}
uniao = conjunto_a.union(conjunto_b)
print(uniao)


x={1,2,3,4}
y={5,6,7,4}

# união
xxx=x|y
print(xxx)

# intersessão
xx=x&y
print(xx)

# diferença
xxxx=x-y
print(xxxx)
xxxx=y-x
print(xxxx)

'''
CONJUNTOS usando set()
'''
'''
O conjunto set() permite outros elementos
'''
from numpy import *
print('aray')
cj=array([2,6,4,5,6,6,6,6,7,7,7,7,7])
print(cj)

print('set() transforma a arry em lista')
cj1=set(cj)
print(cj)

print('tuple() transforma em tupla ()')
cj1=tuple(cj1)
print(cj1)

print('lis() transforma em lista []')
cj1=list(cj1)
print(cj1)

print('set() transforma em conjunto {}')
cj1=set(cj)
print(cj1)

s=x.union(y)
print(s)
