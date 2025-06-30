'''
Problema 1099 - BeeCrowd
Data: 2025.06.26
Autor: Luiz Carlos Oliveira Neto
'''

 #Objetivo: Ler um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

 # Lê a quantidade de casos de teste
n = int(input())

# Para cada caso de teste
for _ in range(n):
    # Lê os dois inteiros X e Y
    x, y = map(int, input().split())

    # Garante que x seja o menor e y o maior
    if x > y:
        x, y = y, x

    soma = 0  # Inicializa a soma

    # Percorre os números entre x e y (exclusivo)
    for i in range(x + 1, y):
        if i % 2 != 0:  # Se for ímpar
            soma += i

    # Imprime a soma dos ímpares entre x e y
    print(soma)