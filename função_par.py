def par_ou_impar(x):
    if x % 2 == 0:
        return True
    else:
        return False


numero = int(input('Qual numero voçê quer saber se é impar ou par? '))

if par_ou_impar(numero) == True:
    print(f'{numero} é par')
else:
    print(f'{numero} é impar')