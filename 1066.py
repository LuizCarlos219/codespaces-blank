'''
Problema 1066 - BeeCrowd
2025/05/25
Luiz Carlos Oliveira Neto
'''

# Objetivo : Ler 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.




# Leitura dos 5 valores inteiros
valores = [int(input()) for _ in range(5)]

# Inicialização dos contadores
pares = impares = positivos = negativos = 0

# Processamento dos valores
for v in valores:
    if v % 2 == 0:
        pares += 1
    else:
        impares += 1
    if v > 0:
        positivos += 1
    elif v < 0:
        negativos += 1

# Impressão dos resultados
print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")