"""
reduce - A partir da versão 3 do python o reduce() não é mais uma função integrada. Para fazer uso desse função é necessário fazer a importação a partir do
módulo 'functools' 

Guido Van Rossum criador do Python diz: Utilize a função reduce() se você realmente precisar dela. Em todo o caso 99% das vezes um loop for é mais legivel

Assim como map() e filter() a função reduce() recebe dois parametros: a função e o interavel

EX: reduce(funcao, dados)

"""

# Vamos utilizar a função reduce() para multiplicar todos os números de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() nos precisamos de uma funcao que receba dois parametros

multiplicacao = lambda x, y: x * y

resultado = reduce(multiplicacao, dados)

print(resultado)

# Utilizando um loop normal

resultado = 1
for n in dados:
    resultado = resultado * n 
print(resultado)