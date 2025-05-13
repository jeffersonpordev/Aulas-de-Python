"""
Introdução ao desempacotamento + tuples (tuplas)

"""



# nomes = ['Maria', 'Helena', 'luiz']
# nome1, nome2, nome3 = nomes
#print(nome2)
# ou
nome1, nome2, nome3 = ['Maria', 'Helena', 'luiz']
print(nome2)

nome1, *resto = ['Maria', 'Helena', 'luiz']
print(nome1, resto)
