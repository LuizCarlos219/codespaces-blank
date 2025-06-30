'''
Problema 1180 - BeeCrowd
Data: 2025.06.26
Autor: Luiz Carlos Oliveira Neto
'''

 #Objetivo:Fazer um programa que leia um valor N. Este N será o tamanho de um vetor X[N]. A seguir, leia cada um dos valores de X, encontre o menor elemento deste vetor e a sua posição dentro do vetor, mostrando esta informação.

 # Lê a quantidade de elementos do vetor
n = int(input())

# Lê os N números como uma lista de inteiros
x = list(map(int, input().split()))

# Encontra o menor valor da lista
menor = min(x)

# Encontra a posição (índice) do menor valor
posicao = x.index(menor)

# Exibe o resultado
print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")