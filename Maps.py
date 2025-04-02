"""
    Maps 
    Com Map fazemos mapeamento de valores para função. Apos a utilização dos dados os mesmos serão removidos da memória após 3 segundos. 
    
"""

import math

def area_circle(r):
    """Calcula a área de um circulo com raio 'R'. """
    return math.pi * (r ** 2)

print(area_circle(2))
print(area_circle(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

#Forma comum

areas = []
for r in raios:
    areas.append((area_circle(r)))
print(areas)

#Forma 2 com uso do Map
#Map é uma função que recebe dois parametros: O primeiro a função e o segundo um interável. Retorna um Map Object. 

areas = map(area_circle, raios)

print(areas)

print(type(areas))

print(list(areas))

