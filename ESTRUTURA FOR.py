
# VARIAVEIS
nome=('joao')
nomes=['joao','jose','paulo']

#================================
# ESTRUTURA FOR COM USO DE STRING
# RETORNA X QUE RECEBE VALOR DE NOME QU É (J,O,A,O)
for x in nome:
    print(x, 'variavel x')
#================================
# ESTRUTURA FOR COM FUNÇÃO STR
# NESSE CASO NÃO PRECISA DECLARAR A VARIAL SEPARDEMENTE
# É SÁ COLOCAR NO PARAMETRO DA FUNÇÃO STR A STRING
for y in str('joao'):
    print(y, 'variavel y')
#================================
# ESTRUTURA FOR COM TABELA
# INFORMAMOS UMA VARIAVEL CHAMADA NOMES QUE CONSTA VARIOS NOMES DETRO DELA
# SERÁ IMPRESSO A LISTA CONSTANTE EM NOMES E SERÁ ATRIBUIDA A R
for r in nomes:
    print(r,'variavel r')
#=================================
# ESTRUTURA IF COM A FUNÇÃO RANGE
# ESTRUTURA DE TABELAS NUMÉRICAS
# SINTAX DE RAGER (<NUMERO INICIAL> , <NUEMRO FINAL>, <NUMERO DE PASSOS>)

# USANDO SOMENTE <NUEMRO UNICIAL> E <NUMERO FINAL>
# RETORNANDO DE 1 ATÉ 8 POIS O NUMERO 9 É OCULTO
for f in range(1,9):
    print(f,'variavel f')
# USANDO SOMENTE <NUEMRO INICIAL> E <NUMERO FINAL>, <PASSOS>
# OU SEJA O LAÇO FOR VAI PERCORRER A TABELA RANGE E DE TRÊS EM TÊS PSSSOS E ARMAZENAR O RESULTADO NA VARIAVEL V
# COM RESULTADO 1
for v in range(1,9,3):
    print(v, ' variavel v')