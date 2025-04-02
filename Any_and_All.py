"""
Any e all

All -> retorna TRUE se todos os elementos do iteraval forem verdadeiros ou ainda se o iteravel está vazio.

#Exemplo all()

print(all([0, 1, 2, 3, 4, 5]))  # O resultado será False pois o Zero não é considerado um valor versadeiro

print(all([1, 2, 3, 4, 5]))  # O resultado será True

print(all([]))  # O resultado será True pois o iteravel no caso a lista está vazio

print(all('Geek'))  # O resultado será True - strings também são validas

#EX_02 all

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina'] # a saida sera true pois todos os elementos começam com C 

print(all([nome[0] == 'C' for nome in nomes]))

#EX_03 all

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Daniel'] # a saida sera False pois nem todos os elementos começam com C 

print(all([nome[0] == 'C' for nome in nomes]))

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Daniel'] # a saida sera False pois nem todos os elementos começam com C 

print(all([nome[0] == 'C' for nome in nomes]))



Any ->  retorna TRUE se qualquer elemento do iteravel for verdadeiro. Se o iteraval estiver vazio retorna false

print(any([0, 1, 2, 3, 4, 5]))  # O resultado será True

print(any([]))  # O resultado será False pois o iteravel no caso a lista está vazio

"""





