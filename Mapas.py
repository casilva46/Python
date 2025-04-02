"""
Mapas: conhecidos em Python como dicionários, os dicionários em Python são representados por {}

"""

#Interar sobre dicionários

receita = {'jan': 100, 'fev': 120, 'mar': 300}

for chave in receita:
    print(chave)
    
for chave in receita:
    print(receita[chave])
    
for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')
    
