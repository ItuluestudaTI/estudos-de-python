#calculo de fatorial
'''n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''

#gerador de progressao aritmetica
'''print('GERADOR DE P.A')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da P.A: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))'''


#sequencia de fibonacci
'''print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print('{} ➪  {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' ➪  {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' ➪  FIM')'''


#exercicio 64
#flag
'''num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: ')) 
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: ')) 
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))'''


'''num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} numeros e a soma entre eles foi {}.'.format(cont, soma))'''


'''resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}.'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))'''