lojas = ['rio de janeiro', 'são paulo', 'salvador']
faturamento = [10000, 20000, 50000]

faturamento.sort
print(faturamento)

print(lojas, faturamento)

for i in range(3):
    tupla = (lojas[i-1], faturamento[i-1])