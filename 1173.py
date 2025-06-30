'''
Problema 1173 - BeeCrowd
Data: 2025.06.26
Autor: Luiz Carlos Oliveira Neto
'''

 #Objetivo:Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10]. Em cada posição subsequente, coloque o dobro do valor da posição anterior. Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente. Mostre o vetor em seguida. 

# Lê o valor inteiro de entrada
v = int(input())

# Cria um vetor de 10 posições
N = [0] * 10

# Preenche a primeira posição com o valor lido
N[0] = v

# Preenche o restante do vetor com o dobro do valor anterior
for i in range(1, 10):
    N[i] = N[i - 1] * 2

# Exibe os valores conforme o formato pedido
for i in range(10):
    print(f"N[{i}] = {N[i]}")
