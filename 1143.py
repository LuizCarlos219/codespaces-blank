'''
Problema 1143 - BeeCrowd
2025/05/14
Luiz Carlos Oliveira Neto
'''
# Objetivo: Mostrar o valor inteiro em sequida  motre numero de 1 a n com seu respectivo valor
# Ler um valor inteiro de n
n = int(input())

# Repetir de 1 a n
for i in range(1,n+1):
# Mostrar o numero com seu respectivo valor elevado ao quadrado e ao Cubo
 print('%d %d %d' %(i, i**2, i**3))