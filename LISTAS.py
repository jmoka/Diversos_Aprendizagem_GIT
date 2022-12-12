import numpy as np
a=np.array([1,2,3,4,5,6])
b=np.array([7,8,9,10,11,12])
print(a)
print(type(a))

zero_array=np.zeros(shape=(5,3,6))
print(zero_array)


zero_array=np.one(shape=(5,3,6))
print(zero_array)

zero_dez=np.arange(10)
print('tfghvnm')
print(zero_dez)
pula_dois=np.arange(3,15,2) # inicia de 3, a quantidade é 15 , as casas são 2 de quanto em quanto
print('wertyhj')
print(pula_dois)

array_linear=np.linspace(0,100, num=4, endpoint=True, retstep=True)
print(array_linear)

print(zero_array.shape) # como a array e construida
print(zero_array.size) # conta a quantidade de casas
print(zero_array.ndim) # linhas
print('hgfjvjbk')
x=a+b
print(x)
c=np.concatenate((a,b))
print(c)
d=np.concatenate((b,a))
print(d)

r=np.array(([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print('hcnbvm')
print(r)
print('__________________________')
print(r[r<8])
print('qwer')
print(r[1:4])

print('mqximo')
print(r.max())
print('minimo')
print(r.min())
print('meio')
print(r.mean())
print('soma')
print(r.sum())


from numpy.random import default_rng

rng=default_rng()
aleatorio=rng.integers(10,size=(2,4))
print('vbnm')
print(aleatorio)

list=[1,'e',4,6,9,8,6,1,0]
listaq=[4,8,0,4,2]
'gjh'
print(list)
s=np.array([1,'df',2,3,7,8,9,0,6,5,0])
print(s)

lista2=([3])
print('wertyu')

lista2.append('q')
print(lista2)

lista2.insert(1,'carro')
print(lista2)

lista2[2]='barco'
print(lista2)

lista2.insert(1,'bebidas')
print(lista2)

lista2.append(listaq)
print(lista2)

lista2.append(len((listaq)))
print(lista2)

lista2.remove('carro')
print(lista2)

lista2.clear()
print(lista2)

l=([1,9,6,0,4])
l1=([8,2,3,7,5])

#ordena
l.sort()
print(l)
#inverte
l.reverse()
print(l)
#conta a quantidade de itens
ll=len(l)
print(ll)
#minimo
lll=min(l)
print(lll)


#soma
lllll=sum(l)
print(lllll)

#média
media=sum(l)/len(l)
print(media)

if 9 in l:
    print('achei')
else:
    print('não achei')

#concatenar
lita3 = l + l1
print(lita3)
#lista repedita
lita4 = l * 4
print(lita4)

# gerando um numero aleatório
from numpy.random import default_rng
rng=default_rng()
aleatorio=rng.integers(1000000000000,size=(1,6))
print(aleatorio)

# compressão de lista
#[item for item in lista]
lista4=[1,2,3,4,5,6,7,8,9]
nova_lista=[item*2 for item in lista4]
print(nova_lista)

# filtro na lista
# [item for in lista if item cond]
'''
no oitem cond coloca-se a condição 
dois exemplos um para encontrar os numeros pares e impares
'''

# nomeros impares
nova_lista1=[item for item in lista4 if item%2==1]
print(nova_lista1)
# nomeros pares
nova_lista1=[item for item in lista4 if item%2==0]
print(nova_lista1)

novaLista=[3/item*2 for item in [1,2,3,4,5,6,7]]
print('wsedr')
print(novaLista)

for i in range(0, len(lista4), 2):
    print(lista4[i])

'''
juntar duas listas.

'''
lista4.extend(l1)
lista4.sort()
print(lista4)


