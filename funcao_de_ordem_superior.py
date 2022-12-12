def selecionador(seq, teste):
    selecionados=[]
    for elemento in seq:
        if(teste(elemento)):
            selecionados.append(elemento)
    return selecionados
def verifica_par(num):
    if num %2==0:
        return True
    else:
        return False

def main():
    lista=[1,2,3,4,5,6,7,8,9]
    pares=selecionador(lista,verifica_par)
    for num in pares:
        print(f'{num} é par')

if __name__=="__main__":
    main()
