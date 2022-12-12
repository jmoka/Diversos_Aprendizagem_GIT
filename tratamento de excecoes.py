try:
    x=int(input('inform um numero:'))
except ValueError:
    print('Inform um Valor Inteiro')
except IndexError:
    print('m2')
except NameError:
    print('O valor informado é diferende de Número')
else:
    print('O valor informado é %d' %(x))

# EXECUTA INDEPENDENTIMENTE DO QUE O CORRER

finally:
  print('executa independetimente do que ocorrer')