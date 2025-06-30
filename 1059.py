'''
Problema 1059 - BeeCrowd
2025.06.26
Luiz.Carlos.Oliveira.Neto
'''

# Fazer um programa que mostre os números pares entre 1 e 100, inclusive.

# Percorre os números de 1 até 100 (inclusive)
for i in range(1, 101):
    # Verifica se o número é par
    if i % 2 == 0:
        # Imprime o número par
        print(i)