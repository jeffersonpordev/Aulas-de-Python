# operadores lógicos
# and (e) or (ou) not (não) 
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor. 
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é  
# usado para representar um não valor

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' or entrada == 'e' and senha_digitada == senha_permitida:
#     print('entrar')
# else:
#     print('sair')


# Avalição de curto circuito

print(True and 0 and True)
print(True or False)
print(True or False or 0)
print(True or False or 0 or 'abc')
print(0 or False or 0 or 'abc' or True)

# usando if com or mas sem usar if

senha = input('senha: ') or 'sem senha' 
print(senha)