'''
Problema 1113 - BeeCrowd
2025.06.25
Luiz.Carlos.Oliveira.Neto
'''

# Ler uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.


while True:
    # Lê uma linha da entrada e divide em duas partes (X e Y)
    x, y = map(int, input().split())

    # Condição de parada: se os valores forem iguais, encerra o loop
    if x == y:
        break

    # Verifica se estão em ordem crescente ou decrescente
    if x < y:
        print("Crescente")
    else:
        print("Decrescente")