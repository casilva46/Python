# Faça um algoritimo que pergunte quanto voce ganha por hora e o numero de horas trabalhadas no mês. Cancule e mostre o total do seu salário no referido mês. 

#entradas

valor_hora = float(input("Qual o valor da hora? "))
horas_trabalhadas = int(input("quantidade de horas trabalhadas "))

# Processamento

salario_mes = (horas_trabalhadas * valor_hora)

# Saida

print("Valor a receber R$ {0:.2f}".format(salario_mes))