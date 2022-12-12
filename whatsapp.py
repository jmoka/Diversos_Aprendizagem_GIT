from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time
import urllib.parse

# =====================================================
# cria o navegador
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

while len(driver.find_elements(By.ID, 'side')) < 1:
    time.sleep(1)
time.sleep(2)

# =====================================================

# WHATSAPP JÁ CARREGOU
# ====================================================
# importar planilha
planilha = pd.read_excel("msg_clietes.xlsx")

# ======================================
# exibir as tabelas
# print(planilha[['cliente' ]]) # dessa forma seleciono somente as colunas que serão exibidas
# print(planilha[['cliente',"numero" ]]) # dessa forma seleciono somente as colunas que serão exibidas
# print(planilha[['cliente', 'msg' ]]) # dessa forma seleciono somente as colunas que serão exibidas
# print(planilha) # exibe planilha completa
# ====================================================

# toda vez que se pensar " para cada ..., para cada tabela ..., para cada item ..." ESTAMSO PENSANDO NO "FOR"

# para casa linha de minha planilha , para isso uso ".index" se for para percorrer as colunas seria ".columns"
# exemplo
# percorrer linha : for linha in planilha.index:
# percorrer coluna for linha in planilha.columns:


for linha in planilha.index:
    # usando ".loc" você precisa iniformar uma lina e uma coluna exe: planilha.loc[linha,coluna] em parentese pois se trata de uma lista
    nome = planilha.loc[linha, 'cliente']
    mensagem = planilha.loc[linha, 'msg']
    telefone = planilha.loc[linha, 'numero']
    # no texto da planilha incluir fulano para ser substituir pelo nome,
    # comando replace("campo de igual ao da msg", pelo que vc que substituir)
    # no caso abaixo fulano texto ficticio que será substituido pelo nome
    texto = mensagem.replace("fulano", nome)
    # o texto dentro de um link tem ser convertido para formato d link
    # paara isso importamos a biblioteca urllib
    texto = urllib.parse.quote(texto)

    # ENVIAR MENSAGEM
    link = f'https://web.whatsapp.com/send?phone={telefone}&text={texto}'
    # ENTRAR NO WHATSAPP NO LINK ACIMA
    driver.get(link)

    # procurar um elemento dentro da pagina que existe somente nela.
    # para isso usamos o find_elements(By.ID, "elemento")
    # devemos usar no plural elements , para que seja retornada uma lista
    '''
    a lógica é a seguinte, usaremos o len para contar se exixte algu elemento com o nome "side" pois esse elemento 
    so existe na página segunte, enquanto não acha o elemento ele espera

    '''
    while len(driver.find_elements(By.ID, 'side')) < 1:
        time.sleep(1)
    time.sleep(2)

    # botão de enviar
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()

    # dar uma pausa de um envio para ou outro
    time.sleep(20)






