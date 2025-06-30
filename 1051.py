'''
Problema 1051 - BeeCrowd
2025/06/25
Luiz Carlos Oliveira Neto
'''

# Objetivo : Lei um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda.


# Lê o salário como número de ponto flutuante
salario = float(input())

# Inicializa o valor do imposto como 0
imposto = 0.0

# Verifica se o salário está na faixa isenta (até R$ 2000.00)
if salario <= 2000.00:
    print("Isento")
else:
    # Cria uma variável auxiliar para calcular o imposto
    excedente = salario

    # Se o salário exceder R$ 4500.00, calcula 28% sobre a parte acima de R$ 4500.00
    if excedente > 4500.00:
        imposto += (excedente - 4500.00) * 0.28
        excedente = 4500.00  # Atualiza o excedente para o limite da faixa anterior

    # Se o salário exceder R$ 3000.00, calcula 18% sobre a parte entre R$ 3000.01 e R$ 4500.00
    if excedente > 3000.00:
        imposto += (excedente - 3000.00) * 0.18
        excedente = 3000.00  # Atualiza o excedente para o limite da faixa anterior

    # Se o salário exceder R$ 2000.00, calcula 8% sobre a parte entre R$ 2000.01 e R$ 3000.00
    if excedente > 2000.00:
        imposto += (excedente - 2000.00) * 0.08

    # Imprime o imposto total com duas casas decimais
    print(f"R$ {imposto:.2f}")