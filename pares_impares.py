import os

with open("pareseimpares.txt", "w", newline='') as arquivo:
    with open('pares.txt') as pares, open('impares.txt') as impares:
        for p,i in zip(pares.readlines(), impares.readlines()):
            arquivo.write(str(p) + str(i))
            