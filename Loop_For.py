"""
    O loop é uma estrutura de repetição e o for é uma dessas estruturas. Utilizamos loops para iterar sequencias ou sobre valores iteraveis.
"""

nome = "Geek University"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)   # temos que trabsformar em uma lista

""" Ex01 de for (Iterando em uma String) """

#for letra in nome:
#    print(letra)


""" EX02 de for (Iterando sobre uma lista) """

#for numero in lista:
#    print(numero)
    
""" EX03 de for (Iterando sobre um range). range(valor_inicial, valor_final) OBS: O valor final não é incluido o processo """

#for numero in range(1, 10):
#    print(numero)

#for valor in enumerate(nome):
#    print(valor)

""" repiticão de loop"""

#qtd = int(input("quantas vezes esse loop deve rodar? "))

#for n in range(1, qtd+1):
#    print(f"Imprimindo {n}")

"""repeticao com soma de entradas

qtd = int(input("quantas vezes esse loop deve rodar? "))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f"Informe o {n}/{qtd} valor: "))
    soma = soma + num
print(f"A soma é {soma}")

"""

""" Imprinmindo saida na mesma linha """

for letra in nome:
    print(letra, end='')








