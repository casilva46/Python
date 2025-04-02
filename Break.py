""" Saindo de loops com o Break. Utilizado para sair de loops de maneira projetada"""

"""EX01

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print("Sai do Loop")

"""

"""EX02"""

while True:
    comando = input("Didite 'sair' para sair: ")
    if comando == 'sair':
        break