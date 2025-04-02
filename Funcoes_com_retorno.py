"""
Funções com retorno

OBS: A palavra reservada return finaliza a função, ela sai da execução da função
     Podemos ter, em uma mesma função diferentes returns
     Podemos em uma função retornar qualquer tipo de dado e até mesmo multiplos valores

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'retorno_de_pop: {ret_pop}'

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

#Ex de função

def quadrado_de_7():
    print(7*7)
    
ret = quadrado_de_7()
print(f'retorno {ret}')   # Essa função irá retornar none. Em Python quando uma função não retorna nenhum valor, o retorno é none. 


#Ex: Vamos refatorar a mesma função para que ela retorne o valor. OBS: refatorar é reescrever o código. 

def quadrado_de_7():
    return 7 * 7     #OBS: Funções em Python que retornam valores, devem retornar estes valores com a palavra reservada return
    
ret = quadrado_de_7()
print(f'retorno {ret}') 


# Vamos criar uma função para jogar uma moeda

from random import random

def joga_moeda():
    valor = random()   #Gera um número pseudo randomico entre 0 e 1 
    if valor > 0.5:
        return 'cara'
    return 'coroa'

print(joga_moeda())

"""

# Testes mão na massa EX1

def mensagem_curso():
    mensagem_curso = 'Geek University'
    return mensagem_curso

print(mensagem_curso())


   

