"""
    Utilizando Lambdas: 
    Conhecidas por expressões Lambdas são funções sem nome ou seja funções anonimas. 
    

# Relembrando o que é uma função em python:

def funcao(x):
    return 3 * x + 1

print(funcao(4))

# Expressão Lambda

lambda x: 3 * x + 1  # OBS: Toda expressão Lambda em Python começa com a palavra reservada lambda

# como utilizar a expressão Lambda

calc_lambda = lambda x: 3 * x + 1  #OBS para utilizar o lambda temos que criar uma variável recebendo a função lambda. 

print(calc_lambda(4))


#Podemos ter expressões Lambdas com multiplas entradas.

#EX

# O .strip remove espaços de inico e fim de uma String
# O .title torna em Maiúsculo o primeiro caracter de uma String

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()  

print(nome_completo(' angelina', 'JOLIE'))
print(nome_completo(' TOM  ', ' HanKS '))

"""






