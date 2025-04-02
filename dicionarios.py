"""
Em algumas linguagens de programação os dicionários Python são conhecidos por mapas, isso porque os dicionários são conhecidos por chave/valor
Dicionários são representados por chaves {}. Tanto a chave qto o valor podem ser de qualquer tipo de dado

EX: {chave:valor}


# criação de dicionários

#Forma 1 - mais comum

paises = {'br':'Brasil', 'us': 'Estados Unidos', 'py':'Paraguai'}
print(paises)
print(type(paises))

#Forma 2 - menos comum

paises_ex2 = dict(br='Brasil', us='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))


#Acessando elementos OBS: dicionários não são indexados

paises = {'br':'Brasil', 'us': 'Estados Unidos', 'py':'Paraguai'}

#Acessando via chave, da mesma forma que via lista/tupla

print(paises['br'])
print(paises['py'])

#Acessando via get - Recomendado

print(paises.get('br'))
print(paises.get('ru'))


# Adicionando novos elementos a um dicionáio. A forma de atualizar um dado ou para iserir um dado é a mesma. Em dicionários NÃO podemos ter chaves repetidas


receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

#forma 1 - mais comum 

receita['abr'] = 350
print(receita)

#forma 2 

novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

# remover dados de um dicionário. 

# forma 1

receita = {'jan': 100, 'fev': 120, 'mar': 300}

receita.pop('mar')   # Obrigatório informar a chave, caso não seja encontrada um keyerror será informado. 
print(receita)

#Forma 2

del receita['fev']
print(receita)

"""





 








