'''
Problema 1078 - BeeCrowd
2025.06.11
Luiz.Carlos.Oliveira.Neto
'''

# Objetivo: Ler os números e fazer uma tabuada do 1 até 10
# Definir o valor de uma variavel para fazer a tabuada
num = int(input())
# Produz uma tabuada com variável anterior
for i in range(1, 11):
    print(f'{i} x {num} = {num*i}')