'''
Problema 2146 - BeeCrowd
Data: 2025.06.26
Autor: Luiz Carlos Oliveira Neto
'''
 #Objetivo:Fazer um programa que, dado um número, informe a respectiva senha.A entrada termina com EOF e a senha é calculada com base em uma regradeduzida dos exemplos fornecidos.

try:
    while True:
        # Lê um número inteiro do crachá
        cracha = int(input())
        # Imprime o valor decrementado em 1
        print(cracha - 1)
except EOFError:
    # Encerra quando não houver mais entrada
    pass