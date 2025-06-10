"""
Introdução às funções (def) em Python
Funções são trechos de códigos usados para 
reolicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e rretornar um valor específico.
Por padrão funções Python retornam None (nada).
"""
# def Print(a, b, c):
#     print('Variaveis1')
#     print('Variaveis2')
#     print('Variaveis3')
#     print('Variaveis4')

# def imprimir(a, b, c):
#     print('Variaveis1', b, c)

# imprimir(1, 2, 3)

def saudacao(nome='sem nome'):
    print(f'ola, {nome}!')

saudacao('jefferson')
saudacao('maria')
saudacao('Fabiola')
saudacao('Guilherme')
saudacao()