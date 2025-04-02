"""
Funções com parametros (de entrada): Funções que recebem dados de entrada para serem processados dentro da mesma. 

    Se pensarmos em um programa qualquer temos: entrada -> processamento -> saida
    
    Se pensarmos em uma função, já sabemos que temos funções que:
        - Nao possuem entrada
        - Não possuem saida
        - Possuem entrada, mas não possuem saida
        - Não possuem entrada,  mas possuem saida
        - Possuem entrada e saida
        - Podem ter vários parametros de entrada, Podemos receber em uma entrada vários parametros desde que estejam separados por ,
        
def quadrado(numero):
    return numero ** 0    # também podria ser feito como numero * numero

print(quadrado(8))
print(quadrado(5))
print(quadrado(9))
print(quadrado(0))

ret = quadrado(6)
print(ret)              # As saidas acima também podem ser escritas dessa forma


# Refatorando a função cantar parabens. 

def cantar_parabens(aniversariante):
    print('Parabéns a você,')
    print('nesta data querida.')
    print('Muitas felicidades,')
    print('muitos anos de vida.')
    print(f'Parabéns {aniversariante}!')
    
cantar_parabens('Marcos')


#Nomeando parametros

def nome_completo(nome, sobrenome):
    return (f'Seu nome completo é: {nome} {sobrenome}')   # Os nomes das funções e das entradas devem fazer sentido para quem as lê. 

print(nome_completo('Brad', 'Pitt'))

"""

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total 

lista = [1, 3, 5, 8, 9, 4, 2, 12, 15]
print(soma_impares(lista))




    


    






