'''
Problema 1044 - BeeCrowd
2025/06/02
Luiz Carlos Oliveira Neto
'''
# Objetivo: SABER SE OS NUMEROS SÃO MULTIPLOS OU NÃO 
# Define as variaveis como numeros
A, B = map(int, input().split())

# Verifica se o numero e numero
if A % B == 0 or B % A == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')