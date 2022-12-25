with open("multiplos de 4.txt", "w") as multiplos_de_4: # Criar e abrir arquivo.
    with open("pares.txt") as pares: # Abrir arquivo existente
        for l in pares.readlines(): #Ler aquivo "pares.txt"
            if (int(l) % 4 ==0): # Selecionar dados
                multiplos_de_4.write(l) # escrever dados selecionados no arquivo "multiplo de 4.txt"