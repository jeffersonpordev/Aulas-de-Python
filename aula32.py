#1
# numero = input('digite um número inteiro: ')

# if numero.isdigit():
#     numero_int = int(numero)
#     par_impar = numero_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'o numero {numero_int} é {par_impar_texto}')

# else:
#     print('você não digitou um número iteiro')


# numero = input('digite um número inteiro: ')

# try:
#     numero_int = int(numero)
#     par_impar = numero_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'o numero {numero_int} é {par_impar_texto}')

# except:
#     print('você não digitou um número iteiro')



# entrada = input('digite a hora: ')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('boa tarde')

#     elif hora >= 18 and hora <= 23:
#         print('boa noite')

#     else:
#         print('não conheço essa hora')

# except:
#     print ('por favo digite numeros inteiros')


nome = input('digite o seu nome:')

nome_str = len(nome)

if nome_str > 1:
    if nome_str <= 4:
        print('seu nome é curto')
    elif nome_str >= 5 and nome_str <= 6:
        print(' seu nome normal')
    else:
        print('seu nome é muito grande')
      
else:
    print('digite mais de uma letra.')
    
    




