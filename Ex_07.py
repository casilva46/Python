# tendo como dados de entrada a altura de uma pessoa. Construa um algoritimo que calcule seu peso ideal usando a formula (72.7 * altura) -58

# Entrada

altura_pessoa = float(input("Informe a altuta da pessoa em metros. "))

# Processamento

peso_ideal = ((72.7 * altura_pessoa) - 58)

# Saida

print ("Seu peso ideal é de {0:.3f}".format(peso_ideal))