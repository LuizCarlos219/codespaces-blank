'''
Problema 1065 - BeeCrowd
2025/05/26
Luiz Carlos Oliveira Neto
'''

# Obejetivo: Fazer um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

# Inicializa o contador de números pares
pares = 0

# Lê 5 valores inteiros, um por vez
for _ in range(5):
    valor = int(input())  # Lê um número inteiro

    # Verifica se o valor é par
    if valor % 2 == 0:
        pares += 1  # Incrementa o contador de pares

# Imprime o resultado no formato exigido
print(f"{pares} valores pares")