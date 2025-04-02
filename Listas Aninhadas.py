"""
Listas Aninhadas

    Algumas linguagens de programação (C, Java, PHP) possuem uma estrutura de dados chamadas de arrays:
        - Unidimensionais (arrays / vetores)
        - Multidimensionais (Matrizes)
    
    Em Python nós temos as Listas
    
        EX: [1, 'b', 3.25, True, 5] - Nesse exemplo o que nas outras linguagens é chamado de array em Python é chamado de lista aninhada.
        

#EX

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  #Matriz 3x3, OBS como em Python não temos as estruturas unidimensionais e multidimensionais nós fazemos uso das listas aninhadas.

print(listas)

print(type(listas))

#Como fazemos para acessar os dados?

print(listas[0][1])   # no exemplo estamos acessando a lista 0 e coluna 1

print(listas[2][1])

# Iterando com loops em lista aninhada

for lista in listas: 
    for num in lista: 
        print(num)
        
"""


        