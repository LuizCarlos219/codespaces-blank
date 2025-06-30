'''
Problema 1073 - BeeCrowd
2025/05/25
Luiz Carlos Oliveira Neto
'''
# Objetivo : Ler um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.

# Lê o valor inteiro N
N = int(input())

# Percorre de 1 até N (inclusive)
for i in range(1, N + 1):
    if i % 2 == 0:  # Verifica se é par
        print(f"{i}^2 = {i**2}")