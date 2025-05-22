"""
split e join com list e str
split - divideuyma string (retorna lista)
join - une uma string
"""

# frase = '     olha só que    , coisa interessante      , meu cachorro latiu       '
# lista_de_frases = frase.split(',')

# for i, frase in enumerate(lista_de_frases):
#     lista_de_frases[i] = lista_de_frases[i].strip()
#     print(lista_de_frases)
#     print(lista_de_frases[i].strip())
# print(lista_de_frases)

frase = '     olha só que    , coisa interessante      , meu cachorro latiu       '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas)
print(lista_frases)

frase = '     olha só que    , coisa interessante      , meu cachorro latiu       '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)

