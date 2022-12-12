'''
# SISTEMA QUE CALCULA A IMC - INDICE DE MASSA CORPORAL
a=eval(input('Informe a sua Altura:'))
p=eval(input('Informe seu Peso:'))

c=(p/a**2)
n1 =18.5
n2=24.9
sp=29.9
ob=30
ob1=40
if c<n1:
    print('Seu índece de massa corporal está muito BAIXO, seu IMC é:',c)
elif c<n2>=n1:
    print('Seu índece de massa corporal está NORMAL, seu IMC é:', c)
elif c<sp>n2:
    print('Seu índece de massa corporal está com SOBREPESO, seu IMC é:', c)
elif c<ob1>=ob:
    print('Seu índece de massa corporal está com OBESIDADE, seu IMC é:', c)
else:
    print('Seu índece de massa corporal está com OBESIDADE GRAVE, seu IMC é:', c)


'''
'FAZENDO DE OUTRA FORMA'

'''
# SISTEMA QUE CALCULA A IMC - INDICE DE MASSA CORPORAL
if c<18.5:
    print('Seu índece de massa corporal está MUITO BAIXO, seu IMC é:',c)
elif c>18.5 and c<24.6 :
    print('Seu índece de massa corporal está NORMAL, seu IMC é:', c)
elif c>24.6 and c<30:
    print('Seu índece de massa corporal está com SOBREPESO, seu IMC é:', c)
elif c>30 and c<40:
    print('Seu índece de massa corporal está com OBESIDADE, seu IMC é:', c)
else:
    print('Seu índece de massa corporal está com OBESIDADE GRAVE, seu IMC é:', c)

'''
'''''
DE OUTRA FORMA USANDO UMA FUNÇÃO
'''''
altura=eval(input('Informe a sua Altura:'))
peso=eval(input('Informe seu Peso:'))


'''
def calculo_imc(peso,altura):
    imc = peso / altura ** 2
    return imc
indice=calculo_imc(peso,altura)
if indice< 18.5:
    print(f'Seu índece de massa corporal está MUITO BAIXO, seu IMC é:{indice}')
elif indice > 18.5 and indice  < 24.6:
    print(f'Seu índece de massa corporal está NORMAL, seu IMC é: {indice}')
elif indice  > 24.6 and indice < 30:
    print(f'Seu índece de massa corporal está com SOBREPESO, seu IMC é: {indice}')
elif indice > 30 and indice  < 40:
    print(f'Seu índece de massa corporal está com OBESIDADE, seu IMC é: {indice}')
else:
    print(f'Seu índece de massa corporal está com OBESIDADE GRAVE, seu IMC é: {indice}')

calculo_imc(peso,altura)
'''

def imc(altura, peso):
    imc = peso / altura ** 2

    if imc <= 18:
        print('muito baixo')
    elif 18< imc <25:
        print('normal')
    elif 26 < imc < 30:
        print('sobre peso ')
    elif 31 < imc < 40:
        print('obeso')
    else:
        print('TA MUITOOOOOO GORDO')

if __name__ == "__main__":
    imc(altura,peso)



