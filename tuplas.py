"""
Tuplas: São muito parecidas com as listas, existem duas diferenças básicas as tuplas são representads por parenteses () e que as Tuplas são imutáveis. Isso significa que depois de criadas não podem ser alteradas, toda a operação em uma tupla gera uma nova.

# Cuidado Tuplas são representadas por (), mas veja. 

tupla1 = (1, 2, 3, 8, 41) # isso é uma tupla

tupla2 = 1, 2, 3, 8, 41 # Isso também é uma tupla

tupla3 = (65) # isso não é uma tupla, cuidaddo com tuplas com apenas 1 elemento

tupla4 = (65,) # isso é uma tupla com apenas um elemento. 

OBS podemos concluir que as tuplas são definidas pelo uso da virgula e não apenas pelo uso dos parenteses.


#Gerando tuplas dinamicamente com a função range. range(inicio, fim, passo) assim como nas listas

tupla_teste = tuple(range(20))
print(tupla_teste)
print(type(tupla_teste))


tupla_teste = tuple(range(1, 10))# com inicio e final
print(tupla_teste)
print(type(tupla_teste))


tupla_teste = tuple(range(3, 20, 3))# com inicio, final e passo
print(tupla_teste)
print(type(tupla_teste))

#Desempacotamento de uma tupla. Assim como na lista as quantidades de elementos devem ser equivalentes

tupla_string = ("Geek University", "Programação em Python")

escola, curso = tupla_string

print(escola)
print(curso)

#metodos para adição e remoção nas tuplas não existem dado o fato das tuplas serem imutáveis.

# Soma*, Maior Valor*, Menor Valor*, tamanho. OBS * Se os valores forem todos inteiros ou reais

tupla1 = (1, 2, 87, 102, 3, 8, 41)

print(sum(tupla1)) # soma
print(max(tupla1)) # Maior valor
print(min(tupla1)) # menor valor
print(len(tupla1)) # Tamanho da lista

#Concatenação de Tuplas

t1 = (1, 2, 3)
t2 = (7, 8, 9)

print(t1)
print(t2)

print(t1 + t2) # as tuplas são imutaveis

t3 = t1 + t2

print(t3)
print(t1)
print(t2)

#Podemos verificar se um determinado elemento está na Tupla

tupla1 = (1, 2, 87, 102, 3, 8, 41)

print(3 in tupla1)

""" 






 





