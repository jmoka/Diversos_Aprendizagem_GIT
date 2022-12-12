"""
FORMATANDO VALORES COM MODIFICADORES

:S  -   Texto (String)
:d  -   Inteiro (int)
:f  -   Número de Ponto Flutuante (float)
:.(Numero)f - Quantidade de Casas Decimais Float
:(> ou < ^)(Quantidade)(tipo - s,d ou f)

>   -   Esquerda
<   -   Direita
^   -   Centro


Função .format()

print('{:}'.format(variavel))

print('{:.3f}'.format(div))

Dentro das chaves coloca-se dois pontos : , sendo que após os dois pontos :. coloca-se um após o ponto
informa a casa quantidade de casas decimais e f


Função f (string)

print(f'{variavel:.2f}')
Da mesma forma que o função format f(string) formada a variavel

"""
nun1=1000
nun2=3
nun3=2
div=nun1/nun2
print(div)  # o resultado é de 3.333333333333335

"""
Uso da função Format
nesse exemplo 3 casas decimais
a {} esta ligada a format da variavel div
"""
print('Formatação usando a Função Format:')
print('{:.3f}'.format(div))
"""
Uso de f(string)
nesse exemplo 2 casas decimais
a {} esta ligada a format da variavel div
"""
print('Formatação usando f(string): ')
print(f'{div:.2f}')

"""
FORMATAÇÃO DE STRING
"""
nome= 'joão luiz'

print(f'{nome:.2s}')

'''
FATIAMENTO DE STRING

'''
# no paramentro antes dos dois pontos é o indice de inicio da estring ou o posicionamento da mesma
# no paramentro depois dos dois pontos é o indice de fim da estring ou o posicionamento da mesma
# podendo ser negativo
print(nome[1:-1])
"""
FORMATAÇÃO DE INCLUSÃO DE VALORES A ESQUERDA
NESSE EXEMPLO INCLUIR 9 ZEROS A ESQUERDA DA VARIAVEL
"""
print(f'{nun3:0>10}') # A ESQUERDA

print(f'{nun3:0<10}') # A DIREITA

print(f'{nun3:0^10}') # CENTRO