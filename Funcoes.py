"""
Funções: são pequenos trechos de código que realizam tarefas especificas. 
        Uma função pode ou não receber entrada de dados
        Muito uteis para executar procedimentos similares por repetidas vezes
    Já utilizamos várias funções desde que iniciamos esse curso:
    
    - Print()
    - len()
    - max()
    - min()
    - count()
    - e varias outras 

# Como definir uma função em Python?
    Em Python de forma geral podemos definir uma função da seguinte forma:
    
def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao



Onde: 

nome_da_funcao -> sempre em letras minúsculas e em caso de nomes compostos utulizar o underline _ (Snake Case)
parametros_de_entrada -> são opcionais, porém qdo tiver mais de um separa-los utilizando a virgula ,
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o procesamento da função acontece. Neste bloco pode ter ou não o retorno da função.

OBS: Veja que para definir uma função fazemos uso da palavra reservada def com isso estamos informando ao Python que iremos iniciar uma função. Também abrimos
o bloco de código utilizando dois pontos :


#Definindo a primeira função

#Definição

def diga_oi():      #Definição e nome da função
    print("Oi!!!")  # Ação a ser executada
    
diga_oi()           #Chamada da função. ATENÇÃO: Nunca se esqueça de utilizar os parenteses () ao executar uma função. 

"""

#EX02

def cantar_parabens():
    print('Parabéns a você,')
    print('nesta data querida.')
    print('Muitas felicidades,')
    print('muitos anos de vida.')
    
for n in range(5):
    print(n)
    cantar_parabens()








