def teste_de_primalidade(valor):
    for x in range(2, valor):
         if valor % x == 0:
             return False
    return True


a = int(input('coloque um numero inteiro: '))

if teste_de_primalidade(a):
    print(f'{a} é primo')
else:
    print(f'{a} não é primo')