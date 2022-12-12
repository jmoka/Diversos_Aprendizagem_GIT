# exemplo de função com duas variaveis
# veja que essa função não retorna nenhum valor não é utilizado a função RETURN
# OBSERVE QUE PECISA INFORMAR OS PARAMETROS PARA QUE SEJA ADICIONADO OS VALORES NAS VARIAVEIS
def saudacao (msg,nome,tipo):
# OBSERVE QUE NO PRINT ELE CHAMA O VALOR DAS DUAS VARIÉVEIS
# AS VARIAVEIS NÃO POSSUEM VALORES PADROES ESTÃO VAZIAS, ATE O MOMENTO QUE É INTRODUZIDO VALOR NELAS NAS LINAS 9 A 13
    print(f'[{msg},{nome},{tipo}] função SAUDAÇÃO sem valor padão na variavel')
# FORA DA FUNÇÃO A MESMA E CHAMADA , OU SEJA A FUNÇÃO ESTÁ SENDO CHAMADA 4 VEZES E NAS QUATRO VEZES ESTÁ SENDO,
# PASSADO PARAMETROS , VALORES NOVOS PARA A VARIAVEL
# IMPRIMINDO 4 VEZES NA TELA OS VALORES INFORMADOS
# OBSERVE QUE A FUNÇÃO NÃO PODE SER CHAMADA SEM ARGUMENTO OU SEM PARAMETRO saudacao(), dessa forma vai dar erro,
# O ERRO ACONTECE POQUE A FUNÇÃO saudadção(msg,nome) NÃO POSSUIM VALOR PADRÃO, E AO SER CHAMADA DA ERRO POR SER VAZIL

saudacao('mensagem', 'tavares', 'macho')
saudacao('23', 'joão', 'macho')
saudacao('show','josé' ,'gay')
saudacao('teste', 'maria','femea')
#============================================================
# Nesse exemplo observe que as variaveis da função já possuem valores ou parêmetros
# Dessa forma a função pode ser chamda ser que seja passado valor para a mesma
def despedida (msg='CHAL', nome='vazil', tipo='indeciso'):
    print(f'{msg},{nome},{tipo} função DESPEDIDA com valor padão na variavel')
# Observe que ao chamer a função não fui passado nenhuma unformação ou parametro ,
# # com isso a função utilizará dos valores ou parametros padrões onde msg=CHAL, nme=vazil
despedida()
# LEMBRANDO QUE SE FORM PASSADO O PARAMETRO NOVO PARA A VARIAVEL, A MESMA ASUMIRÁ OS VALORES NOVOS
despedida('bay-bay','Marcel', 'confuso')

#==========================================================

# IREMOS VER COMO PODEMOS INVERTER OS VALORES DAS VARIÁVEIS DAS FUNÇÕES DE FORMA ESPECÍFICA
# VAMOS APROVEITAR AS DUAS FUNÇÕES ACIMA FUNÇÃO 'SAUDAÇÃO E FUNÇÃO 'DESPEDIDA'
# OBSERVE QUE IREMOS FAZER OS CHAMADOS DAS FUNÇÕES PASSADO ESPECIFICAMENTE QUAL PARAMETRO QUERO MUDAR

despedida(nome='zezinho', msg='bay-bay', tipo='bichona')
#(OBSERVE QUE OS VALORES FORAM TROCADOS DE FORMA CORRETA NA FUNÇÃO)


from Calculadora import soma, mutiplicacao, subtracao,divisao
print(soma(2,3))
print(mutiplicacao(4,5))



