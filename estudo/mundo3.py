#ex 72
'''cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[num]}')'''

#ex 73
'''times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Curitiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O chapecoense está na {times.index("Chapecoense")+1}ª posição')'''

#ex 74
'''from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')'''

#ex 75

    