'''
Problema 1079 - BeeCrowd
2025.06.26
Luiz.Carlos.Oliveira.Neto
'''

# Objetivo: Ler 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal. Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.

# Lê o número de casos de teste
n = int(input())

# Laço que será repetido 'n' vezes, uma para cada caso de teste
for _ in range(n):
    # Lê uma linha com três valores separados por espaço e divide em uma lista de strings
    valores = input().split()
    
    # Converte os três valores da lista para float (números decimais)
    v1, v2, v3 = map(float, valores)
    
    # Calcula a média ponderada:
    # v1 tem peso 2, v2 tem peso 3, v3 tem peso 5
    # Soma os produtos e divide pela soma dos pesos (10)
    media = (v1 * 2 + v2 * 3 + v3 * 5) / 10
    
    # Imprime o resultado da média formatado com uma casa decimal
    print(f"{media:.1f}")