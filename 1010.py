'''
Problema 1010 - BeeCrowd
2025/05/21
Luiz Carlos Oliveira Neto
'''

# Objetivo: ler o codigo quantidade e valor
# Ler o codigo valor da peça 1
cod, qtdP1, valP1 = input().split(' ')
qtdP1 = int(qtdP1) # converte qtdP1 para int
valP1 = float(valP1) # converte valP1 para float
# Ler o codigo valor da peça 2
cod, qtdP2, valP2 = input().split(' ')
qtdP2 = int(qtdP2) # converte qtdP2 para int
valP2 = float(valP2) # converte valP2 para float
# Calcular o valorPagar
vPagar = (qtdP1*valP1) + (qtdP2*valP2)

# Mostrar a msg VALOR A PAGAR com 2 casas decimais
print('VALOR A PAGAR: R$ %.2f' %vPagar)