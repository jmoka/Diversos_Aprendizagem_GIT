def AreaQuadrado(l,a):
    area = l*a
    return area
lado=eval(input('informe o valor do lado:'))
altura=eval(input('informe o valor da altura:'))
area=AreaQuadrado(lado,altura)
print(f'a Área do quadrado é {area} métros quadrados')