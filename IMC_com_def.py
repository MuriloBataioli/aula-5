def obter_entrada(mensagem):
    entrada = float(input(mensagem))
    while entrada <= 0:
        print('Entrada inválida! Tente novamente.')
        entrada = float(input(mensagem))
    return entrada

print('Olá usuario vamos calcular seu IMC')

nome = str(input('Qual é o seu nome? '))
peso = obter_entrada('Seu peso em kg: ')
altura = obter_entrada('Sua altura em metros: ')

imc = peso / altura**2

if imc > 15 and imc < 18.55:
    print(f'{nome}, você está abaixo do peso!!')
elif imc >= 18.55 and imc < 24.55:
    print(f'{nome}, você está no seu peso normal')
elif imc >= 24.55 and imc < 29.55:
    print(f'{nome}, você está acima do peso!!')
print(imc)
