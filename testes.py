from random import randint as rd
def letrasenums(n=0, l=0):
    senha = []
    for i in range(0, n):
        senha.append(rd(0, 9))
    for c in range(0, l):
        s = chr(rd(65, 90))
        senha.insert(rd(0, len(senha)-1), s)
    for d in senha:
        print(i, end= ' ')
