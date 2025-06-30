'''
Problema 1176 - BeeCrowd
Data: 2025.06.26
Autor: Luiz Carlos Oliveira Neto
'''

 #Objetivo:Fazer um programa que leia um valor e apresente o número de Fibonacci correspondente a este valor lido. Lembre que os 2 primeiros elementos da série de Fibonacci são 0 e 1 e cada próximo termo é a soma dos 2 anteriores a ele. Todos os valores de Fibonacci calculados neste problema devem caber em um inteiro de 64 bits sem sinal.

 # Lê a quantidade de casos de teste
t = int(input())

# Cria um vetor com os 61 primeiros números de Fibonacci (0 a 60)
fib = [0] * 61
fib[1] = 1

# Preenche o vetor com os valores da sequência de Fibonacci
for i in range(2, 61):
    fib[i] = fib[i - 1] + fib[i - 2]

# Para cada caso de teste, lê o valor N e imprime o Fibonacci correspondente
for _ in range(t):
    n = int(input())
    print(f"Fib({n}) = {fib[n]}")