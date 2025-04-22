"""
Repetiçoes
While (enquanto)
Executa uma ação enauqnto uma condição for verdadeira
loop infinito -> quando o codigo não tem fim
"""
condicao = True

while condicao:
    nome = input(f'qual sdeu nome: ')
    print(f'seu nome é {nome}\n')

    if nome =='sair':
        break

print('acabou')



