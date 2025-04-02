""" 
Listas: listas em Python funcionam como vetores/matrizes (arrays em outras linguagens), com a diferença de seram DINAMICO e também de podermos colocar QUALQUER tipo de dado. As listas em Python são representadas por colchetes []

    - Dinanmico: Não possui tamanho fixo; ou seja podemos criar uma lista e simplesmente ir adicionando elementos. 
    - Qualquer tipo de dados: Não possuem tipo de dado fixo; podemos colocar qualquer tipo de dado.
    - Em uma lista os elementos são separados por virgula ,
"""

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

""" 
Podemos facilmente checar se um valor está contido em uma lista

num = int(input("Digite um numero" ))

if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Não encontrei o numero {num}')


# Podemos facilmente ordenar uma lista

lista1.sort()
print(lista1)


# Podemos facilmente ordenar Strings em uma lista

lista5.sort()
print(lista5)

# Podemos facilmente contar o numero de ocorrencias em uma lista

print(lista1.count(1))
print(lista5.count('e'))



# Adicionando elementos em uma lista
# Para adicionar elementos em uma lista utilizamos a função append, OBS: com o append nós só conseguimos adicionar um elemento por vez

print(lista1)
lista1.append(145)
print(lista1)


# Adicionando elementos em uma lista. Uma lista dentro de outra lista

print(lista1)
lista1.append([87, 12, 52])   #coloca a lista como como elemento único uma especie de sublista
print(lista1)

num = int(input("Digite um numero" ))

if num in lista1:
    print(f'Encontrei o numero {num}')
else:
    print(f'Não encontrei o numero {num}')
    

print(lista1)
lista1.extend([222, 91, 51])  #coloca cada novo elemento da lista como um valor adicional na lista. OBS esse tipo de inserção na funciona com valor único
print(lista1)

num = int(input("Digite um numero" ))

if num in lista1:
    print(f'Encontrei o numero {num}')
else:
    print(f'Não encontrei o numero {num}')
    
# podemos adicionar um novo elemento na lista informando a posição do indice
# Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista

print(lista1)
lista1.insert(2, 'N')   #coloca a lista como como elemento único uma especie de sublista
print(lista1)

#podemos facilmente juntar duas lists

lista1 = lista1 + lista2    ou  lista1.extend(lista2)

#Invertendo a ordem de apresentação de uma lista

lista1.reverse()       ou     print(lista1[::-1])

#copiando uma lista

lista6 = lista2.copy()
print(lista6)

#Podemos Saber qtos elementos tem em uma lista

print(len(lista1))

#Podemos remover o último elemento de uma lista

lista1.pop()

#Podemos remover um elemento de uma lista pelo indice. Caso não houver elemento no indice informado teremos o erro index error

lista1.pop(2)

#Podemos remover todos os elementos de uma lista

lista1.clear()

#Podemos converter uma String em uma lista

curso = 'Programaçaõ em Python'
print(curso)
curso = curso.split()    #O split() separa os elementos de uma lista através do espaço
print(curso)

#Podemos converter uma String em uma lista, utilizando a visgula como separador

curso = 'Programacao,em,Python'
print(curso)
curso = curso.split(',')    #O split(',') separa os elementos de uma lista através da virgula
print(curso)


# com for

cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores)
for cor in cores:
    print(cor)
    
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
    
    
# criando um indice em um for

cores = ['verde', 'amarelo', 'azul', 'branco']

for indice, cor in enumerate(cores):
    print(indice, cor)
    
# Soma*, Maior Valor*, Menor Valor*, tamanho. OBS * Se os valores forem todos inteiros ou reais

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

print(sum(lista1)) # soma
print(max(lista1)) # Maior valor
print(min(lista1)) # menor valor
print(len(lista1)) # Tamanho da lista

# Transformar uma lista em uma Tupla

lista_teste = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

print(lista_teste)
print(type(lista_teste))

tupla_teste = tuple(lista_teste)
print(tupla_teste)
print(type(tupla_teste))

# desempacotamento de lista. OBS se tivermos mais elementos do que variáveis para receber teremos "error value" e o contrário também é vslido
lista_teste = [1, 99, 4]

n1, n2, n3 = lista_teste

print(n1)
print(n2)
print(n3)

# copiando os dados de uma lista para outra. Veja que ao utilizarmos lista_teste.copy() para a nova lista não houve alteração da lista_teste. Ou seja uma lista não afeta a outra. Isso em Python é chamado de DEEP COPY

lista_teste = [1, 99, 4]
print(lista_teste)

nova_lista_teste = lista_teste.copy()
print(nova_lista_teste)

nova_lista_teste.append(58)

print(lista_teste)
print(nova_lista_teste)

"""



















