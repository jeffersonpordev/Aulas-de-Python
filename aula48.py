"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - Índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update   Delete = (CRUD)
Criar, Ler, alterar, apagar = lista[i] (CRUD)
"""
#       01234
#      -54321
# string = 'ABCDE' # 5 caracteres (len)



# #         0     1       2          3    4       
# #        -5    -4      -3         -2   -1       
# lista = [123, True, 'jefferson', 1.2, []]
# lista[-3] = 'fabiola'


# print(lista)
# print(lista[0], type(lista[0]))
# print(lista[1], type(lista[1]))
# print(lista[2], type(lista[2]))
# print(lista[3], type(lista[3]))
# print(lista[4], type(lista[4]))
# print(lista[-5])
# print(lista[-4])
# print(lista[-3])
# print(lista[-2])
# print(lista[-1])

lista = [10, 20, 30, 40]
lista[2] = 300
del lista[2]
print(lista)
print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop()
print(lista, 'Removido,', ultimo_valor)

