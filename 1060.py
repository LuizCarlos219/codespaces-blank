'''
Problema 1060 - BeeCrowd
2025.06.26
Luiz.Carlos.Oliveira.Neto
'''

# Objetivo:Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.


# Inicializa o contador de valores positivos
positivos = 0

# Lê 6 valores (que podem ser float), um por linha
for _ in range(6):
    valor = float(input())  # Lê um número real

    # Verifica se o valor é positivo (maior que zero)
    if valor > 0:
        positivos += 1  # Incrementa o contador

# Imprime o total de valores positivos
print(f"{positivos} valores positivos")