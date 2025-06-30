'''
Problema 1134 - BeeCrowd
2025/06/26
Luiz Carlos Oliveira Neto
'''
# Objetivo : O Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o código informado for o número 4.

# Inicializa os contadores para cada tipo de combustível
alcool = 0
gasolina = 0
diesel = 0

while True:
    codigo = int(input())  # Lê o código digitado pelo usuário

    if codigo == 1:
        alcool += 1  # Incrementa o contador de álcool
    elif codigo == 2:
        gasolina += 1  # Incrementa o contador de gasolina
    elif codigo == 3:
        diesel += 1  # Incrementa o contador de diesel
    elif codigo == 4:
        break  # Encerra o programa
    # Se o código for inválido (≠ 1, 2, 3, 4), apenas ignora e continua pedindo entrada

# Exibe o resultado conforme o formato solicitado
print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")