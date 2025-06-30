'''
Problema 1072 - BeeCrowd
Data: 2025.06.26
Autor: Luiz Carlos Oliveira Neto
'''

 #Objetivo:Fazer um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em seguida mostre o vetor X.

 # Cria um vetor vazio
X = []

# Lê 10 valores inteiros
for i in range(10):
    valor = int(input())
    
    # Se o valor for menor ou igual a 0, substitui por 1
    if valor <= 0:
        valor = 1
    
    X.append(valor)  # Adiciona o valor ao vetor

# Imprime o vetor conforme o formato exigido
for i in range(10):
    print(f"X[{i}] = {X[i]}")