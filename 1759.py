'''
Problema 1759 - BeeCrowd
2025.06.25
Luiz.Carlos.Oliveira.Neto
'''

# Objetivo: trabalho é ajudar o Papai Noel montando um problema que mostre todos os "Ho" que ele deve falar dado o número sorteado.

# Lê um número inteiro N da entrada, que representa quantas vezes "Ho" será falado
N = int(input())

# Gera uma lista com N elementos "Ho" e junta todos eles com um espaço, depois adiciona "!" no final
saida = ' '.join(['Ho'] * N) + '!'

# Imprime a saída final
print(saida)