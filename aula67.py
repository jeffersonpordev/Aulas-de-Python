"""
Valores padrão para parâmetros
ao definir uma função, os parâmetros podem 
tr valores padrão. Caso o valor não seja
enviado ára o parâmetro, o valor padrão será usado.
Refatorar: edityar o seu codigo.
"""

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=}, {y=}, {z=}', x + y + z)
    else :
        print(f'{x=}, {y=}', x + y)
    print( x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)
