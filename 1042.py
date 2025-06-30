'''
Problema 1042 - BeeCrowd
2025/06/25
Luiz Carlos Oliveira Neto
'''

# Obejetivo:Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.


# Lê a entrada como uma única linha e separa em três inteiros
valores = list(map(int, input().split()))

# Guarda a ordem original
original = valores.copy()

# Ordena os valores
valores.sort()

# Imprime os valores ordenados
for v in valores:
    print(v)

# Imprime uma linha em branco
print()

# Imprime os valores na ordem original
for v in original:
    print(v)