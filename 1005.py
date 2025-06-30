'''
Problema 1005 - BeeCrowd
2025/05/19
Luiz Carlos Oliveira Neto
'''

# Objetivo: Calcular a media de um aluno

# Ler 2 valores == Notas A e B == Tipo float
A = float(input())
B = float(input())

# Calcular peso das Notas de A e B
A = A*3.5
B = B*7.5

# Calcular a Media
Media = (A+B)/11
# Mostrar a msg Media e etc.
print("MEDIA = %.5f" %Media)