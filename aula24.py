# Operadores in  e not in
# Strings em python são iteraveis
# 0 1 2 3 4 5 6 7 8
# J e f f e r s o n
# -8-7-6-5-4-3-2-1

nome = 'jefferson'
# print(nome[2])
# print(nome[-5])
# print(nome[3])
# print(nome[-2])
# print ('r' in nome) # tem a letra no nome por isso True
# print ('a' in nome) # Não tem a letra no nome por isso False
# print ('ers' in nome) # tem as letras em seguidas no nome por isso True
# print ('jers' in nome) # Não tem as letras em seguidas no nome por isso False

nome =  input('digite seu nome: ')
encontrar = input('digite oque deseja encontra: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')


