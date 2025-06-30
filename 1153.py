'''
Problema 1153 - BeeCrowd
2025.06.26
Luiz.Carlos.Oliveira.Neto
'''

# Objetivo: Ler um valor N. Calcular e escrever seu respectivo fatorial

# Lê o valor inteiro N
n = int(input())

# Inicializa a variável fatorial com 1 (neutro da multiplicação)
fatorial = 1

# Laço que vai de 1 até N (inclusive)
for i in range(1, n + 1):
    fatorial *= i  # Multiplica o valor atual do fatorial por i

# Imprime o resultado final
print(fatorial)