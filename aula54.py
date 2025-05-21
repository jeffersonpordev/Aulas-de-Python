"""
Faça uma lista de comprar com listas 
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permit que o programa quebre com 
erros de indíces inexistentes na lista.
"""
import os

lista = []

while True:
    print('selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('valor: ')
        lista.append(valor)
        print('i')
    elif opcao == 'a':
        if len(lista) == 0: 
                print('Nada para apagar')
                os.system('cls')
        

        indice_str = input('Escolha o índice para pagar: ')
        
        try :
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Não foi possível apagar este índice')
        except IndexError:
            print('Ìndice não existe na lista')
    elif opcao == 'l':
            os.system('cls')

            if len(lista) == 0: 
                print('Nada para listar')

            for i, valor in enumerate(lista):
                print(i, valor)
   