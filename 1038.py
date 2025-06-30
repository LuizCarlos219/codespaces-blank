'''
Problema 1038 - BeeCrowd
2025.06.11
Luiz.Carlos.Oliveira.Neto
'''

# Objetivo:Leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.
# Executa o preço do produto em variveis e faz o trotal do produto a pagar
def main():
    item, quantidade = input().split()
    item = int(item)
    total = 0
    quantidade = int(quantidade)
    if item == 1:
        total = quantidade * 4
    elif item == 2:
        total = quantidade * 4.5
    elif item == 3:
        total = quantidade * 5
    elif item == 4:
        total = quantidade * 2
    elif item == 5:
        total = quantidade * 1.5
    print('Total: R$ %.2f'% total)
main()