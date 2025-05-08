"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - Índices e fatiamento
Métodos úteis: 
    append - Adiciona um item ao final 
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena lista
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
nome = lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop()
lista.append(1233)
del lista[-1]
#lista. clear()
lista.insert(3, 5)
lista.insert(9, 58)# o primeiro numeo é o local e o segundo numero é o valor # sempre que for adicionar em um local que não existe na lista, sempre sera alocado no final da lista
#print(lista[90]) # sempre que acessar um local que não existe na lista, acontecera um erro.
print(lista, 'Removido,', ultimo_valor, nome)

