"""  
Calculo de Media, Variancia e Desvio Pradrão

"""

import numpy as np

# Entrada de dados

numeros = [3, 4, 30, 37, 46, 53]

# Calculos
media = np.mean(numeros)
variancia = np.var(numeros)
desvio_padrao = np.std(numeros)

# Exebição dos resultados
print()
print("Os numeros informados foram:", numeros)
print()
print("Média:", media)
print()
print("Variância:", variancia)
print()
print("Desvio Pradrão:", desvio_padrao)