"""
Conjuntos
    Conjuntos em qualquer linguagem de programação, estamos nos referindo a Teoria dos conjuntos da matemática. 
    
Em Python conjuntos são chamados de sets. Dito isso, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados
- Sets (conjuntos) não possuem valores ordenados
- Elementos não são acessados via indice, ou seja conjuntos não são indexados

Conjuntos são bons para se utilizar quando precisamos armazenar elementos, mas não nos importamos com a ordenação deles. Quando não precisamos nos 
preocupar com chaves, valores e itens duplicados. 

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferenças entre conjuntos (sets) e Mapas (dicionários) em Python:

- Um dicionário tem pares de chave:valor
- Um conjunto tem apenas o valor


#Definindo um conjunto

# Forma 1 

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # repare que existem valores repetidos
print(s)
print(type(s))

#OBS: Ao criar um conjunto com valores repetidos, os valores repetidos serão ignorados sem gerar erro

# Forma 2 - mais comum  

s = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}
print(s)
print(type(s))


# Convertendo lista, tuplas e dicionários em sets(dicionários)

lista = [1, 2, 3, 4, 5, 5, 6, 7, 2, 3]
conjunto = set(lista)
print(conjunto)

if 9 in conjunto:
    print('tem o 9 no conjunto')
else:
    print('Não tem o 9 no conjunto')

#Adicionando elementos em um conjunto

conjunto_teste = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}
print(conjunto_teste)

conjunto_teste.add(4) # Duplicidade não gera erro, simplesmente é ignorado
print(conjunto_teste)

#Removendo dados de um conjunto

#Forma 1

conjunto_teste = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}
print(conjunto_teste)

conjunto_teste.remove(4) # Não é indice, informamos o valor a ser removido
print(conjunto_teste)

#Forma 2

conjunto_teste.discard(5)
print(conjunto_teste)

#Copiando um conjunto para outro

#Forma 1 - Deep Copy

conjunto_teste = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}

novo_teste = conjunto_teste.copy()
print(novo_teste)

novo_teste.add(99)
print(novo_teste)
print(conjunto_teste)

#Forma 2 Shallow Copy

conjunto_teste = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}
print(conjunto_teste)

novo_teste = conjunto_teste    # = Informa que as duas variaveis terão os mesmos valores, se uma for alterada a outra também será. 
conjunto_teste.add(888)

print(novo_teste)
print(conjunto_teste)

#Podemos remover todos os dados de um conjunto

conjunto_teste = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}
print(conjunto_teste)

conjunto_teste.clear()
print(conjunto_teste)

#Metodos matemáticos do conjuntos

# Metodos Matemáticos em conjuntos

"""

# Imagine que temos dois conjuntos, um contendo alunos que fizeram o curso de Python e outro contendo os alunos que fizeram o curso de Java

estudantes_python = {'marcos', 'Patricia', 'Carlos', 'Arthur', 'Heitor', 'Julia', 'Ellen'}
estudantes_java = {'Fernando', 'Gustavo', 'Maria', 'Carlos', 'Patricia', 'Arthur'}

# Veja que alguns alunos que estudaram Java também estudaram python
# Precisamos gerar um conjunto com nomes únicos

# Forma 1 - Utilizando o comando Union  (forma mais recomendada)

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

"""""

#Forma 2 - Utilizando o caracter pipe |

unicos2 = estudantes_python | union(estudantes_java)

#Gerar uma lista de estudantes que estão em ambos os cursos

#Forma 1 - com o comando intersection

estudantes_python = {'marcos', 'Patricia', 'Carlos', 'Arthur', 'Heitor', 'Julia', 'Ellen'}
estudantes_java = {'Fernando', 'Gustavo', 'Maria', 'Carlos', 'Patricia', 'Arthur'}

print(estudantes_python)
print(estudantes_java)

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

#Forma 2 - com o comando &

estudantes_python = {'marcos', 'Patricia', 'Carlos', 'Arthur', 'Heitor', 'Julia', 'Ellen'}
estudantes_java = {'Fernando', 'Gustavo', 'Maria', 'Carlos', 'Patricia', 'Arthur'}

print(estudantes_python)
print(estudantes_java)

ambos2 = estudantes_python & estudantes_java
print(ambos2)

#Gerar conjuntos de estudantes que estão matriculados em um unico curso

estudantes_python = {'Marcos', 'Patricia', 'Carlos', 'Arthur', 'Heitor', 'Julia', 'Ellen'}
estudantes_java = {'Fernando', 'Gustavo', 'Maria', 'Carlos', 'Patricia', 'Arthur'}

somente_java = estudantes_java.difference(estudantes_python)
print('estudantes de Java {}' .format(somente_java))

somente_python = estudantes_python.difference(estudantes_java)
print('estudantes de Python {}' .format(somente_python))

"""
































