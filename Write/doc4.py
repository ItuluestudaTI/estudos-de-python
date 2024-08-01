'''valor = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quandos anos de financiamento? '))
prestacao = valor / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos. '.format(valor, anos), end='')
print(' A prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO! ')
else:
    print('Empréstimo NEGADO!')'''
    
#num = int(input('Digite um número: '))
#print('''Escolha uma das bases de conversão:
#[ 1 ] converter para BINÁRIO
#[ 2 ] converter para OCTAL
#[ 3 ] converter para HEXADECIMAL''')
#opçao = int(input('Sua opção: '))
#if opçao == 1:
 #   print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
#elif opçao == 2:
 #   print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
#elif opçao == 3:
 #   print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
#else:
 #   print('Opção inválida. Tente novamente')
 
'''num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro valor: '))
if num1 > num2:
    print('O PRIMEIRO valor é maior.')
elif num1 == num2:
    print('Os valores são iguais!')
else:
    print('O SEGUNDO valor é maior.')'''
    
    
    
    
'''from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento militar'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi no ano {}'.format(ano))'''
    
    
'''nota1 = float(input('primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f},  média do aluno é {:.1f}'.format(nota1, nota2, media))
if media >= 5 and media < 7:
    print('O aluno está em RECUPERAÇÃO.')
elif media < 5:
    print('O aluno está REPROVADO')
elif media >= 7:
    print('O aluno está APROVADO')'''
    
    
'''from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')'''
    
    
'''r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
        
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')'''
    
    
'''peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE, cuidado!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')'''
    
print('{:=^40}'.format('  LOJAS AMARANTE  '))
preco = float(input('Preço das compras: R$'))
print('''FORMA DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} no final.'.format(totparc, parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))




    

