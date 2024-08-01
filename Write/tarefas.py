'''tarefas = []

tarefa = input('Insira uma tarefa ')
tarefas.append(tarefa)
print(tarefas)

while tarefa != '':
    tarefa = input('Insira uma tarefa ')
    tarefas.append(tarefa)
    
print(tarefas[2:])'''

'''i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('FIM')'''

'''s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'. format(s))'''


'''from time import sleep
print('{:=^40}'.format('  CONTAGEM REGRESSIVA  '))

for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('PEI PEI PEI POW POW!')'''

'''from time import sleep
for cont in range (2, 51, 2):
    print(cont, end=' ')
    sleep(0.3)
print('Acabou')'''

'''soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma dos {} valores solicitados é de {}.'.format(cont, soma))'''


'''num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:.2f} = {}'.format(num, c, num*c))'''
 
'''soma = 0
cont = 0   
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1   
if cont == 1:
    print('Você informou {} número PAR e a soma foi {}'.format(cont, soma))
else:
    print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))'''
 
    

'''primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end='  ➡  ')
print('ACABOU')'''

'''from time import sleep
for c in range(10, 0, -1):
    print(c)
    sleep(0.3)
print('fim')'''


'''numint = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, numint + 1):
    if numint % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')

if numint == 1:
    print('\n\033[mO número {} foi divisível {} vez'.format(numint, tot))
else:
    print('\n\033[mO número {} foi divisível {} vezes'.format(numint, tot))

if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')'''
    
    
'''frase = str(input('Digite uma frase: ')).strip().upper() #lendo a frase #upper é maiuscula
palavras = frase.split() #dividindo a frase (splitando) gerando listas
junto = ''.join(palavras) #juntando as listas pra eliminar os espaços antes e depois
print('Você digitou a frase {}'.format(junto)) #juntado tudo numa unica string 
inverso = junto[::-1]

#for letra in range(len(junto) - 1, -1, -1): #aqui é o loop que coloca o inverso da frase
    #inverso += junto[letra] #outra forma de fazer
    
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALíNDROMO!')
else:
    print('A frase digitada NÃO é um PALÍNDROMO!')'''
  
  
'''from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))'''


''' somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
    
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))'''   




    
    

