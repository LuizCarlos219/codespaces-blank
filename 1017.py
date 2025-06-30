'''
Problema 1017 BeeCrowd
2025/06/25
Luiz.Carlos.Oliveira.Neto
'''
# Objetivo:Calcular o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).
# Cria variaveis H e V 
H=int(input())
V=int(input())

# Cria uma Variavel para aparecer o resultado da Multiplicação de H e V
Km_Total = H * V
# Faz o comsumo = Km_total
comsumo = Km_Total / 12
# Mostra na tela o resuiltado
print('{:.3f}'.format(comsumo))