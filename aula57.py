"""
lista de listas e seus índices
"""
salas = [
    # 0     , 1
    ['Maria','Helena', ],           #0
    # 0     , 1
    ['Elaine', ],                   #1
    # 0     , 1
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30,40) ],  #2
]

print(salas)
print(salas[1])
print(salas[1][0])
print(salas[0][1])
print(salas[2][2])
print(salas[2][3][3])

for sala in salas:
    print(sala)

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)