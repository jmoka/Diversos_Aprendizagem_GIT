import math
x=eval(input('informe um numero:'))
y=eval(input('informe um numero:'))
'''
função math.sqrt retorna a raiz quadrada
'''
print(f'função math.sqrt retorna a raiz quadrada, no sado de apenas o x que foi informado {x}')
x = math.sqrt(x)
print(x)
#====

'''
obter o logaritmo de base 2 do numro, aceita u nomero e retorna o logaritimo da bese 10 do numero fornecido
'''
print(f'a função math.log10 obter o logaritmo de base 2 do numero, aceita u nomero e retorna o logaritimo da bese 10 do numero fornecido, apenas o x que foi informado {x}')
z=math.log10(x)
print(z)

'''
eleva o valor a mesma potencia , retorna o valor de x  elevado a potencia y
'''
print(f' função math.pow , sendo x={x} e y={y} eleva o valor a mesma potencia , retorna o vaalor de x  elevado a potencia y')
s=math.pow(x,y)
print(s)



