'''
Problema 1070 - BeeCrowd
2025.06.26
Luiz.Carlos.Oliveira.Neto
'''

# Objetivo: Ler um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.


# Lê o valor inteiro X
x = int(input())

# Se X for par, somamos 1 para começar do próximo número ímpar
if x % 2 == 0:
    x += 1

# Imprime os próximos 6 ímpares
for i in range(6):
    print(x + i * 2)