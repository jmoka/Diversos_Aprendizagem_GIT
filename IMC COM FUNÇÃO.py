#Cabeçalho da função, inicia com 'def'.
# DOIS PARAMETROS FORAM PASSADOS O PESO E A ALTURA
# SENDO O PESO O PARAMETRO A SER INFORMADO
def imc(peso, altura=0):
    altura=eval(input('digite sua altura:\n'))
    calculo=(peso/altura**2)
    return calculo
# NESSE MOMEMNTO PEDE PARA O USUARIO INFORMAR O VALOR DE SEU PESO, QUE SERA USADO COMO PARAMETRO DA FUNÇÃO
pess=eval(input('qual a peso:\n'))
# OBSERVE QUE AO CHAMAR A FUNÇÃO IMC FOU INFORMADO O PARAMETRO PESS QUE É O NUMERO INFORMADO ANTERIORMENTE
resultado = imc(pess)

n1 =18.5
n2=24.9
sp=29.9
ob=30
ob1=40
if resultado<n1:
    print('Seu índece de massa corporal está muito BAIXO, seu IMC é:',resultado)
elif resultado<n2>=n1:
    print('Seu índece de massa corporal está NORMAL, seu IMC é:', resultado)
elif resultado<sp>n2:
    print('Seu índece de massa corporal está com SOBREPESO, seu IMC é:', resultado)
elif resultado<ob1>=ob:
    print('Seu índece de massa corporal está com OBESIDADE, seu IMC é:', resultado)
else:
    print('Seu índece de massa corporal está com OBESIDADE GRAVE, seu IMC é:', resultado)