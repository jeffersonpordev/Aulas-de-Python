"""
introdução ao try/excepty
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input('vou dobrar o numero que você digtar: ')

try: 
    print('STR: ', numero_str)
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
    
except:
    print('isso nao é um numero')
