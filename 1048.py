'''
Problema 1048 BeeCrowd
2025/06/25
Luiz.Carlos.Oliveira.Neto
'''

# Objetivo: Ler o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

# Cria uma variavel
salario = float(input())

# Determina o percentual de reajuste com base no salário
if salario <= 400.00:
    percentual = 15
elif salario <= 800.00:
    percentual = 12
elif salario <= 1200.00:
    percentual = 10
elif salario <= 2000.00:
    percentual = 7
else:
    percentual = 4

# Calcula o reajuste e o novo salário
reajuste = salario * (percentual / 100)
novo_salario = salario + reajuste

# Imprime os resultados com duas casas decimais
print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")