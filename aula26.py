"""
FOrmatação básica de strings
s - string
d - int
f - float
.<número de dígitos> f
x ou X - Hexadecimal
(Cararctere)(><^)(quntidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0> -100, 1.f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}.')
print(f'{variavel:$^10}.')
print(f'{variavel:z^10}.')
print(f'{156.1515111:.2f}.')
print(f'O hexadecimal de 1500 é  {1500:08X}')



