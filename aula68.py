"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
o escopo global é o escopo onde todo o código é alcançavel.
O escopo local éo escopo onde apenas nomes do mesmo local podem ser alcançados.
"""

x = 1

def escopo():
    def outra_funcao():
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


escopo()