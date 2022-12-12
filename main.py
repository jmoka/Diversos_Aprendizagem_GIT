#================================================
# CALCULANDO NUMERO NA BASE 10 PARA OUTRAS BASES
#================================================
# BIBLIOTECAS
from tkinter import *
janela1=Tk()
#------------------------------------
# VARIAVEIS
base10=0
largura=400
altura=325

#--------------------------------

#---------------------------------
# ENTRY
txb=Entry(janela1,
            # bg="#80bfff",
            # fg="#000000",
            font="Arial 12 bold italic",
            width=20,  # largura
            bd=5, # Borda
            relief='groove',
# Tipo da borda solid, groove, flat, raised, sunken, ridge
            # anchor=N, # Posicionamento da strig sendo posicionado pelas letras N, S , L , W,CENTER, SW
           justify=LEFT # CENTER, RIGHT, LEFT
           )
#------------------------------------------------
# FUNÇÕES BASE 10 PARA OUTRAS BASES

def binario():
    b2=(f'Convertido para BINÁRIO é: {bin(base10) [2:]}')
    return b2
 # DE BASE 10 PARA OCTAL
def octal ():
    b8=(f'Convertido para OCTAL é: {oct(base10) [2:]}')
    return b8
 # DE BASE 10 PARA HEXADECIMAL
def hexadecimal ():
    b16=(f'Convertido para HEXADECIMAL é: {hex(base10) [2:]}')
    return b16
#----------------------------------------------
# WIDEETS
    # TÍTULO DA JANELA
janela1.title('Missão Prática | Nível 2')
    # LABEL TEXTO DO CABEÇALHO
# VARIÁVEIS
    # ATRIBUIÇÃO NAS VARIANTES LARGULA1 E ALTURA1 OS VALORES DO FORMULÁRIO
    # ATRAVÉS DA FUNÇÃO  winfo_screenwidth e winfo_screenheight
largura1=janela1.winfo_screenwidth()
altura1=janela1.winfo_screenheight()

#---------------------------------------------
# POSICIONAMENTO DA JANELA CENTRALIZADO
posicao_x=largura1/2-largura/2
posicao_y=altura1/2 - altura/2

# ---------------------------------------------
# GEOMETRIA (geometry)
    # DIMENCIONA A JANELA LARGURA X ALTURA + POSIÇÃO(X) + POSIÇÃO(Y) (L X A + X + Y)
janela1.geometry(f"%dx%d+%d+%d" % (largura, altura, posicao_x,posicao_y))

#----------------------------------
# PRIMEIRA LABEL
label1=Label(janela1,
            text='Sistema de Conversão Entre Bases',
            font='Arial 16 bold italic', # fonte
            # bg="#ffffff", # Cor do fundo
            fg="#1a8cff", # Cor da linha
            width=30, # largura
            height=1, # Altura
           # bd=1, # Borda
           # relief='solid', # tipo da borda solid, groove, flat, raised, sunken, ridge
            anchor=N, # Posicionamento da strig sendo posicionado pelas letras N,NS, NW, S, SW, SE, E , W,CENTER
            padx=2,
            pady=2,
            justify=CENTER # CENTER, RIGHT, LEFT
             )
#-------------------------------------------
# SEGGUNDA LABEL
label2=Label(janela1,
            text='''Converter da Base 10 para as Bases\n(Binária,Octal e Hexadecimal)''',
            font='Arial 16 bold',
            # bg="#ffffff",
            fg="#000000",
            # width=30,  # largura
            # height=5,  # Altura
            bd=5, # Borda
            relief='groove', # Tipo da borda solid, groove, flat, raised, sunken, ridge
            anchor=CENTER, # Posicionamento da strig sendo posicionado pelas letras N, NE, NW, S, SW, SE, E , W,CENTER
            padx=10,
            pady=19,
            justify=CENTER # CENTER, RIGHT, LEFT
             )
#----------------------------------------
# TERCEIRA LABEL
label3=Label(janela1,
            text='Digite um Número Inteiro:',
            font='Arial 12 bold',
            # bg="#ffffff",
            fg="#000000",
            # width=30,  # largura
            # height=5,  # Altura
            bd=5, # Borda
            relief='groove', # Tipo da borda solid, groove, flat, raised, sunken, ridge
            # anchor=W, # Posicionamento da strig sendo posicionado pelas letras N, NE, NW, S, SW, SE, E , W,CENTER
            padx=1,
            pady=1,
            # justify=LEFT # CENTER, RIGHT, LEFT
             )
#-----------------------------------------------
# LABEL BINARIO
label_b=Label(janela1,
              text='BINÁRIO:',
              font='Arial 12 bold',
              # bg="#ffffff",
              fg="#000000",
              width=40,  # largura
              height=1,  # Altura
              # bd=5, # Borda
              # relief='groove', # Tipo da borda solid, groove, flat, raised, sunken, ridge
              anchor=W,  # Posicionamento da strig sendo posicionado pelas letras N, NE, NW, S, SW, SE, E , W,CENTER
              padx=1,
              pady=1,
              # justify=LEFT # CENTER, RIGHT, LEFT
              )
#----------------------------------------------
# LABEL OCTAL
label_o=Label(janela1,
            text='OCTAL:',
            font='Arial 12 bold',
            # bg="#ffffff",
            fg="#000000",
            width=40,  # largura
            height=1,  # Altura
           # bd=5, # Borda
           # relief='groove', # Tipo da borda solid, groove, flat, raised, sunken, ridge
            anchor=W, # Posicionamento da strig sendo posicionado pelas letras N, NE, NW, S, SW, SE, E , W,CENTER
            padx=1,
            pady=1,
           # justify=LEFT # CENTER, RIGHT, LEFT
             )
#----------------------------------------------------
# LABEL HEXADECIMAL
label_h=Label(janela1,
              text='HEXADECIMAL:',
              font='Arial 12 bold',
              # bg="#ffffff",
              fg="#000000",
              width=40,  # largura
              height=1,  # Altura
              # bd=5, # Borda
              # relief='groove', # Tipo da borda solid, groove, flat, raised, sunken, ridge
              anchor=W,  # Posicionamento da strig sendo posicionado pelas letras N, NE, NW, S, SW, SE, E , W,CENTER
              padx=1,
              pady=1,
              # justify=LEFT # CENTER, RIGHT, LEFT
              )
#--------------------------------------
# lABEL INFORMAÇÃO BASE 10
label_b10=Label(janela1,
              text='DECIMAL:',
              font='Arial 12 bold',
              # bg="#ffffff",
              fg="#000000",
              width=40,  # largura
              height=1,  # Altura
              # bd=5, # Borda
              # relief='groove', # Tipo da borda solid, groove, flat, raised, sunken, ridge
              anchor=W,  # Posicionamento da strig sendo posicionado pelas letras N, NE, NW, S, SW, SE, E , W,CENTER
              padx=1,
              pady=1,
              # justify=LEFT # CENTER, RIGHT, LEFT
              )
#--------------------------------------
# lABEL ARTE
label_art=Label(janela1,
                bg="#80bfff",
                text="Faculdade Estácio de Sá, Full Stack",
                font='Arial 12 bold'
                )
 #------------------------------------------
# BOTÃO (BUTTTON)
    # Exemplo usando o LAMBDA, observe que ao chamar a função informaei os parenteses
    # e por isso a necessidade de usar o LAMBDA
btn=Button(janela1,
            text='Calcular',
            bg="#80bfff",
            fg="#000000",
            font="Arial 16 bold italic",
            width=30,  # largura
            height=1,  # Altura
            bd=1, # Borda
            relief='solid', # Tipo da borda solid, groove, flat, raised, sunken, ridge
            anchor=N, # Posicionamento da strig sendo posicionado pelas letras N, S , L , W,CENTER, SW
# Dessa forma não há necessidade de informar o LAMBDA ao chamar a função é só informar sem os parenteses
# btn=Button(janela1,text='Calcular', command=resultado
           command=lambda:apresentar(),
            # padx=10,
            # pady=19,
            justify=CENTER # CENTER, RIGHT, LEFT
           )
#---------------------------------
# SET FOCUS
txb.focus()

#---------------------------------
 # POSICONONAMENTO NO GRID
    # POSICIONAMENTO DAS WIDTS
label1.grid(row=0, column=0, sticky=W)
label2.grid(row=1, column=0, sticky=W)
label3.grid(row=2, column=0, sticky=W)
label_art.grid(row=3, column=0, sticky='we')
txb.grid(row=2, column=0, sticky=E)
label_b10.grid(row=4, column=0, sticky=W)
label_b.grid(row=5, column=0, sticky=W)
label_o.grid(row=6, column=0, sticky=W)
label_h.grid(row=7, column=0, sticky=W)
btn.grid(row=9, column=0, sticky='we')

#----------------------------------
# FUNÇÃO APRESENTAR AS INFORMAÇÕES
def apresentar1():
    label_b10['text'] = (f'Base Decimal: {base10}')
    label_b['text'] = binario()
    label_o['text'] = octal()
    label_h['text'] = hexadecimal()

def apresentar():
    global base10
    try:
        base10 = int(txb.get())
        label_art['text'] = str("Faculdade Estácio de Sá, Full Stack")

    except ValueError:
        label_art['text']=str('Opss. um Erro: ( Informe um Número Inteiro)')
        label_b10['text'] = 'BASE DECIMAL:'
        label_b['text'] = 'BINÁRIO:'
        label_o['text'] = 'OCTAL'
        label_h['text'] = 'HEXADECIMAL'

    else:
        apresentar1()








#---------------------------------

#-----------------------------------
# CHAMADA DA FUNÇÃO TKINTER
janela1.mainloop()






