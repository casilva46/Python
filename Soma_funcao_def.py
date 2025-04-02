"""
    Soma de duas variaveis com função soma 
"""

def sum(a, b):
        return(a + b)
    
a = int(input('Digite um valor para A: '))
b = int (input('Digite um valor para B: '))

print(f'A soma de {a} e {b} é igual a {sum(a, b)}')