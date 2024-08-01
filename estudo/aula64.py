#break aula 15 mundo 2
'''n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')'''

'''e = 33
salario = 987.35
print(f'O {nome} tem {idade} anos e ganha R${salario}')'''

#ex 66
'''num = cont = 0
soma = 0
while True:
    num = int(input('Digite um número: [999 para parar]: '))
    if num == 999:
        break
    soma += num
    cont += 1
    
print(f'{cont} números foram digitados e a soma entre eles foi {soma}.')'''


#ex 67
'''while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('TABUADA ENCERRADA')'''

#ex 68
'''from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
    elif tipo == 'I':
        print('Você PERDEU!')
        break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! você venceu {v} vezes.')'''

#ex 69
'''tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN': 
        resp = str(input('Quer continuar? [S/N]  ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres com menos de 28 anos.')'''


#ex 70
'''total = totmil = menor = 0
cont = 0
barato = 0
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:10.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')'''

#ex 71
'''print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Qual o valor a ser sacado? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} notas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre!')'''

#aula 16 Estruturas compostas
'''lanche = ('Hamburgueres', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')'''

#lanche = ('Hamburgueres', 'Suco', 'Pizza', 'Pudim', 'Batat frita')

#for cont in range(0, len(lanche)):
    #print(f'Eu vou comer {lanche[cont]} na posição {cont}')

#for pos, comida in enumerate(lanche):
    #print(f'Eu vou comer {comida} na poisção {pos} ' )
#print('comi pra caramba')

#print(sorted(lanche))

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(5, 1))'''

'''pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)'''

