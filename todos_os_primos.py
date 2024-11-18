def teste_de_primalidade(valor):
    for x in range(2, valor):
         if valor % x == 0:
             
             return False
    return True


numero = int(input('Escreva um numero inteiro: '))
for x in range(2, numero+1):
    if teste_de_primalidade(x):
        print(f'{x} é primo')
#não consegui pensar em uma solução