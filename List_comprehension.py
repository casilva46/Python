"""
List Comprehension - podemos gerar novas listas a partir de outro interavel. 

# Sintaxe da list Comprehension [dado for dado in interavel]

#EX

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

#Para entender melhor o que está acontecendo devemos dividir a experssao em duas etapas:
# primeira parte: for numero in numeros
# Segunda parte: numero * 10

res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]

print(res)

EX

# List Comprehension x Loop

#Loop

numeros_dobrados = []
for numero in [1, 2, 3, 4, 5]:
    numeros_dobrados.append(numero * 2)
    
print(numeros_dobrados)

# List Comprehension

print([numero * 2 for numero in [1, 2, 3, 4, 5]])

"""






