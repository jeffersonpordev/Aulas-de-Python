"""
enumerate - enumera iteráveis (índices)
"""

lista =['maria', 'helena', 'luiz']
lista.append('João')

# for indice, nome in enumerate(lista):
#     print(indice, nome)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice)

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')