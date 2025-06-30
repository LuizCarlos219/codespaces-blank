'''
Problema 1014 BeeCrowd
2025/06/16
Luiz.Carlos.Oliveira.Neto
'''
# Objetivo:Calcular o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).
# Cria variaveis X e Y e divide eles com uma varivel de Km
X=int(input())
Y=float(input())
Km=X/Y
# Faz aparecer o resultado da divisão e mostra o km
print(f'{Km:.3f} km/l')