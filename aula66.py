"""
Argumenetos nomeados e não nomeados em funções Python
Argumenetos nomeados tem nome com sinla de igual
Argumenetos não nomeados recebe apenas o argumento(valor)
"""

def soma(x, y):
    print(f' {x=} y={y}', '|', 'x + y = ', x + y)

soma(1, 4)
soma(y=4, x=1)

print(1, 2, sep='-')

