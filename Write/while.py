'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')'''


'''n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par  += 1
        else:
            impar += 1
print('Você digitou {} numeros pares e {} numeros impares'.format(par, impar))'''


'''sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, Informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))'''


'''from random import randint
from time import sleep
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 a 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            sleep(0.3)
            print('Mais... Tente novamente')
        elif jogador > computador:
            sleep(0.3) 
            print('Menos... Tente novamente')
print('Acertou! com {} tentativas.'.format(palpites))'''



