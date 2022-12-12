# FUNÇÃO FIBONACCI

def fibonacci(num):
    if num<=1:
        return num
    else:
        return fibonacci (num-1) + fibonacci (num-2)
x = int(input('Digite um número para Calcular Fibonacci \n'))
res=fibonacci(x-1)
print('O fibonacci de %d é %d' % (x,res))




