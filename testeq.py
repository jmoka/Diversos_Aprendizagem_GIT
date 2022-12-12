from tkinter import *
janela1=Tk()
base10=0
largura=400
altura=325


txb=Entry(janela1,
            font="Arial 12 bold italic",
            width=20,
            bd=5,
            relief='groove',
           justify=LEFT
           )

def binario():
    b2=(f'Convertido para BINÁRIO é: {bin(base10) [2:]}')
    return b2

def octal ():
    b8=(f'Convertido para OCTAL é: {oct(base10) [2:]}')
    return b8

def hexadecimal ():
    b16=(f'Convertido para HEXADECIMAL é: {hex(base10) [2:]}')
    return b16
janela1.title('Missão Prática | Nível 2')
largura1=janela1.winfo_screenwidth()
altura1=janela1.winfo_screenheight()

posicao_x=largura1/2-largura/2
posicao_y=altura1/2 - altura/2

janela1.geometry(f"%dx%d+%d+%d" % (largura, altura, posicao_x,posicao_y))


label1=Label(janela1,
            text='Sistema de Conversão Entre Bases',
            font='Arial 16 bold italic',
            fg="#1a8cff",
            width=30,
            height=1,
            anchor=N,
            padx=2,
            pady=2,
            justify=CENTER
             )
label2=Label(janela1,
            text='''Converter da Base 10 para as Bases\n(Binária,Octal e Hexadecimal)''',
            font='Arial 16 bold',
            fg="#000000",
            bd=5,
            relief='groove',
            anchor=CENTER,
            padx=10,
            pady=19,
            justify=CENTER
             )

label3=Label(janela1,
            text='Digite um Número Inteiro:',
            font='Arial 12 bold',
            fg="#000000",
            bd=5, # Borda
            relief='groove',
            padx=1,
            pady=1,
            )
label_b=Label(janela1,
               text='BINÁRIO:',
              font='Arial 12 bold',
              fg="#000000",
              width=40,
              height=1,
              anchor=W,
              padx=1,
              pady=1,
              )
label_o=Label(janela1,
            text='OCTAL:',
            font='Arial 12 bold',
            fg="#000000",
            width=40,
            height=1,
            anchor=W,
            padx=1,
            pady=1,
            )
label_h=Label(janela1,
              text='HEXADECIMAL:',
              font='Arial 12 bold',
              fg="#000000",
              width=40,
              height=1,
              anchor=W,
              padx=1,
              pady=1,
              )
label_b10=Label(janela1,
              text='DECIMAL:',
              font='Arial 12 bold',
              fg="#000000",
              width=40,
              height=1,
              anchor=W,
              padx=1,
              pady=1,
              )

label_art=Label(janela1,
                bg="#80bfff",
                text="Faculdade Estácio de Sá, Full Stack",
                font='Arial 12 bold',
                fg='#000000'
                )
btn=Button(janela1,
            text='Calcular',
            bg="#80bfff",
            fg="#000000",
            font="Arial 16 bold italic",
            width=30,
            height=1,
            bd=1,
            relief='solid',
            anchor=N,

           command=lambda:apresentar(),

            justify=CENTER
           )

txb.focus()
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
        label_art['fg']='#000000'

    except ValueError:
        label_art['text']=str('Opss. um Erro: ( Informe um Número Inteiro)')
        label_art['fg']='#ff0000'
        label_b10['text'] = 'BASE DECIMAL:'
        label_b['text'] = 'BINÁRIO:'
        label_o['text'] = 'OCTAL'
        label_h['text'] = 'HEXADECIMAL'

    else:
        apresentar1()
        


janela1.mainloop()

