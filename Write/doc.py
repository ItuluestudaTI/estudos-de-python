lista = ['banana', 'maçã', 'laranja']
print(lista[-3])

lista.append('beterrada')
print(lista)

lista.insert(2, 'chocolate')
print(lista)

del lista[4]
print(lista)

lista.append('carro')
print(lista)

lista_sonhos = []
sonho = lista.pop(-1)
print(sonho)

lista_sonhos.append(sonho)
print(lista)
print(lista_sonhos)