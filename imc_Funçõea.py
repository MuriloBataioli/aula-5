def calcula_imc(altura, peso):
    imc = peso / altura**2
    return imc


def classificação_imc(imc):
    if imc < 15:
        return 1
    elif imc >= 15 and imc < 18.95:
        return 2
    elif imc >= 18.95 and imc < 24.95:
        return 3
    elif imc >= 24.95 and imc < 29.95:
        return 4


def pegar_peso():
    peso = float(input('Seu peso em kg: '))
    while peso <= 0:
        print('Peso invalido!')
        peso = float(input('Seu peso em kg: '))
    return peso


def pegar_altura():
    altura =  float(input('Sua altura em metros: '))
    while altura <= 0:
        print('altura invalida!')
        altura =  float(input('Sua altura em metros: '))
    return altura


minha_altura =pegar_altura()
meu_peso = pegar_peso()
meu_imc = calcula_imc(minha_altura, meu_peso)
classificação = classificação_imc(meu_imc)
print(meu_imc)
if classificação == 1:
    print('magreza extrema')
elif classificação == 2:
    print('abaixo do peso')
elif classificação == 3:
    print('peso normal')
elif classificação == 4:
    print('acima do peso')
else:
    print('classificação desconhecida')