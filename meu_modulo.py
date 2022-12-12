def dados():
    peso = print(eval(input('informe o peso:')))
    altura =  peso=print(eval(input('informe o altura:')))
    imc = peso / altura**2
    return imc

def condicao(imc):
    if imc < 18.5:
         return (f'Seu índece de massa corporal está MUITO BAIXO, seu IMC é:{imc}')
    elif imc > 18.5 and imc < 24.6:
         return (f'Seu índece de massa corporal está NORMAL, seu IMC é: {imc}')
    elif imc  > 24.6 and imc < 30:
         return (f'Seu índece de massa corporal está com SOBREPESO, seu IMC é: {imc}')
    elif imc > 30 and imc  < 40:
         return (f'Seu índece de massa corporal está com OBESIDADE, seu IMC é: {imc}')
    else:
         return (f'Seu índece de massa corporal está com OBESIDADE GRAVE, seu IMC é: {imc}')




