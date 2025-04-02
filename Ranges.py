""" Entendendo Ranges. São utilizados para gerar sequencias numéricas não de forma aleatória mas sim de maneira especificada.
Formas gerais:

- range (valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1) """

"""Forma 1

for num in range(11): # é o caso de n-1. nesse caso irá imprimir até 10
    print(num, end= " ") # OBS end= " " - imprime o resultado na mesma linha com espaço entre os caracteres

"""

"""Forma 2

range(valor_inicio, valor_parada)

OBS: valor_parada não inclusive (inicio especificado e passo de 1 em 1)

for num in range(65, 100): # é o caso de n-1. nesse caso irá imprimir até 10
    print(num, end= " ") # OBS end= " " - imprime o resultado na mesma linha com espaço entre os caracteres

""" 

"""Forma 3 

range(valor_inicio, valor_parada, passo)

OBS: valor_parada não inclusive (inicio especificado e passo de 2 em 2); O passo pode ser alterado

for num in range(0, 100, 2): # é o caso de n-1. nesse caso irá imprimir até 10
    print(num, end= " ") # OBS end= " " - imprime o resultado na mesma linha com espaço entre os caracteres

""" 

"""Forma 4 (inversa)

range(valor_inicio, valor_parada, passo)

OBS: valor_parada não inclusive (inicio especificado e passo de 2 em 2); O passo pode ser alterado """

for num in range(10, 0, -2): 
    print(num) 









