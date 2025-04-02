"""
sorted 
OBS: Não confundir, apesar do nome com a função sort() que já vimos em listas. O sort() só funciona em listas equanto que o sorted() funciona com qualquer iterável. 
como o próprio nome diz sorted() serve para ordernar. 

OBS: o sort() modifica a lista
     o sorted() não modifica a lista original e cria uma nova. O sorted() sempre irá retornar uma lista com os elementos que foram ordenados.
"""

#EX

numeros = [6, 1, 8, 14, 89, 51]
print(numeros)

print(sorted(numeros))  #Ordenar do menor para o maior

print(sorted(numeros, reverse=True)) # Ordena do maior para o menor

print(numeros)