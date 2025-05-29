# desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helene', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# a, b, *_, u = lista
# print(a, u)

print(*lista)
print(*string)
print(*tupla)

for nome in lista:
    print(nome, end=' ')

