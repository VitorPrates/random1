from senhas import funcoes as fc
from random import randint as rd

num = int(input('Quantos numeros?[0 para não adicionar números]:'))
letras = int(input('Quantas letras?[0 para não adicionar letras]:'))

if num > 0 and letras == 0:
    fc.numeros(num)
if num == 0 and letras > 0:
    fc.apenasletras(letras)
if num > 0 and letras > 0:
    fc.letrasenums(num, letras)
if num == 0 and letras == 0:
    print('deseja criar senha aleatória?')
    resp = str(input('[S / N]:'))[0].lower()
    if resp =='s':
        fc.letrasenums(rd(0, 5), rd(0, 5))
#K0RV78H2 minúsculo
#D:\vitor\python\instalador