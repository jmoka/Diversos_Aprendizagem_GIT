x = eval(input('Informe sua Idade \n'))
def teste():

    if x<=0:
        y = x + 1
        print(f'Valor foi: {y}')
        return y

    else:
        y = x + 2
        print(f'Valor foi: {y}')

        return y


print(teste())

