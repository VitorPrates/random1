import random as rd


def numeros(num=0):
    senha = []
    for c in range(0, num):
        senha.append(rd.randint(1, 9))
    for i in senha:
        print(i, end='')


def apenasletras(letras=0):
    senha = []
    for c in range(0, letras):
        senha.append(chr(rd.randint(65, 90)))
    for i in senha:
        print(i, end='')


def letrasenums(n=0, l=0):
    senha = []
    for i in range(0, n):
        senha.append(rd.randint(0, 9))
    for c in range(0, l):
        s = chr(rd.randint(65, 90))
        senha.insert(rd.randint(0, len(senha) - 1), s)
    for d in senha:
        print(d, end='')
