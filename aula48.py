"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - Índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#       01234
#      -54321
string = 'ABCDE' # 5 caracteres (len)



#         0     1       2          3    4       
#        -5    -4      -3         -2   -1       
lista = [123, True, 'jefferson', 1.2, []]
lista[-3] = 'fabiola'


print(lista)
print(lista[0], type(lista[0]))
print(lista[1], type(lista[1]))
print(lista[2], type(lista[2]))
print(lista[3], type(lista[3]))
print(lista[4], type(lista[4]))
print(lista[-5])
print(lista[-4])
print(lista[-3])
print(lista[-2])
print(lista[-1])


