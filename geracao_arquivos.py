with open('ímpares.txt','w') as impares, open('pares.txt','w') as pares:
        for n in range(0,100):
            if (n % 2 ==0):
                pares.write(f'{n}\n')
            else:
                impares.write(f'{n}\n')
