'''

parametros principais
papel(0) x tesoura(1) = 0+1 tesoura(1)
pepel(0) x pedra(-1) = 0-1 papel(0)
papel ==1
tesoura >2
pedra<2 and pedra >1

empate pedra = 0
empate tesoura ==4
empate papel == 2

#EMPATE#
TESOURA(2) X TESOURA(2) = 4
PEDRA(0) X PEDRA(0) = 0
PAPEL(1) X PAPEL(1) = 2
'''
from random import randint
# variavais
# valores
pedra=0
papel=1
tesoura=2
# aponentes
jogador=0
computador=0

def inicio():
    global jogador
    while (1):
        jogador = int(input('ESCOLHA UMA DAS OPÇÕES ABAIXO \n (0) Pedra\n (1) Papel\n (2) Tesoura\n'))
        if jogador>2:
            print('ESCOLHA ERRADA, TROQUE DE NUMERO')
        else:
            print('JOGADOR ESCOLHEU', jogador)
            jogadapc()
        break

def parar():
    while (1):
        p=int(input('ESCOLHA UMA DAS OPÇÕES ABAIXO \n (0) SAIR\n (1) JOGAR NOVAMENTE\n'))
        if p==0:
            print('MUITO OBRIGADO POR JOGAR')
        elif p==1:
            inicio()
        else:
            print('OPÇÃO ERRADA, ESCOLHA OUTRO NÚMERO')
            parar()
        break



def resultado ():
    result=soma()
    if jogador == computador:
        print('DEU EMPATE, ESCOLHA OUTRA OPÇÃO')
        parar()
    elif result==1:
        print('PAPEL GANHOU')
        parar()
    elif result<=2:
        print('PEDRA GANHOU')
        parar()
    elif result > 2 or result <= 3:
        print('TESOURA GANHOU')
        parar()

def soma():
    soma=jogador+computador
    return soma

def jogadapc():
    global computador
    computador=randint(0,2)
    print('O COMPUTADOR ESCOLHEU,', computador)
    resultado()

def saudação():
    print('JOGO PEDRA, PAPEL e TESOURA\n(_MUITO OBRIGADO POR TESTAR_)')
    p = int(input('ESCOLHA UMA DAS OPÇÕES ABAIXO \n (0) SAIR\n (1) JOGAR NOVAMENTE\n'))
    if p==0:
        print('MUITO OBRIGADO POR TESTAR O NOSSO JOGAR')
    elif p==1:
        print('INÍCIO DO JOGO')
        inicio()
    else:
        print('OPÇÃO ERRADA, ESCOLHA OUTRO NÚMERO')
        saudação()
saudação()


