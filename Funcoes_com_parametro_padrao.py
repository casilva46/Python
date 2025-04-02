"""
Funções com parametros Padrão (default) - Funções onde a passagem de parametros é opcional. Funções são pequenos trechos de código que realizam tarefas especificas. Podem ou receber entrada de dados e retornar uma saída, são muito uteis para executar procedimentos similares repetidas vezes. 



EX de função com passagem obrigatória do parametro

def quadrado(numero):
    return numero ** 2      

print(quadrado(3))   # Passagem do parametro é obrigatória

print(quadrado())    # Se não passar o parametro irá dar erro 


# EX de função com com valor padrão

def exponencial(numero,potencia=2):    #nessa função definimos o valor default como 2; onde potencia=2
    return numero ** potencia

print(exponencial(2, 3))

print(exponencial(3, 2))

print(exponencial(3))    #aplicou o valor default

print(exponencial(3, 5))

OBS: em Python valores default devem sempre estar no final da declaração

"""

#EX mais complexo

def mostra_informacao(nome="Geek", instrutor=False):
    if nome == "Geek" and instrutor:
        return "Bem vindo instrutor Geek!!"
    elif nome == "Geek":
        return "Eu pensei que fosse o instrutor Geek"
    return f"Ola {nome}"

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao("Ozzy"))
print(mostra_informacao(nome="Stephany"))





        