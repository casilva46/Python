"""
    Programa que seleciona 15 números de forma aleatória de 01 a 25 para apostas na Lotofacil
    Data Criação 05/04/2024

"""

import random

def selecionar_numeros():
    numeros = random.sample(range(1, 26), 15)
    numeros_ordenados = sorted(numeros)
    return numeros_ordenados

if __name__ == "__main__":
    numeros_selecionados = selecionar_numeros()
    print("Números selecionados em ordem crescente:", numeros_selecionados)