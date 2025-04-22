"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entrega o próximo valor
iter -> me entrega seu iterador
"""

numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)
