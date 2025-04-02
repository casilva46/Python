# Algoritimo para calcular o IMC

# Entradas

#nome = ("Informe o seu nome: ")
peso = float(input("Informe o seu peso em Kg "))
altura = float(input("Informe a sua altura em metros "))

# Processamento

imc = (peso/((altura)**2))

# Saida

print ("O seu imc é de {0:.2f}".format(imc))

if imc <18.5:
    print("Abaixo do peso")  
elif imc >18.5<=24.9:
    print("Peso normal")  
elif imc >25.0>=29.9:
    print("Sobrepeso") 
elif imc >30.0<=34.9:
    print("Obesidade")
else:
    print("Obesidade morbida")

