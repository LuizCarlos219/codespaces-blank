'''
Problema 1018 BeeCrowd
2025/06/25
Luiz.Carlos.Oliveira.Neto
'''
# Objetivo :

# Cria uma lista
def main():
    valor= int(input())
    print(valor)
    nota_100 = valor // 100
    valor = valor % 100
    print('%d nota(s) de R$ 100,00'% nota_100)

    nota_50 = valor // 50
    valor = valor % 50
    print('%d nota(s) de R$ 50,00'% nota_50)

    nota_20 = valor // 20
    valor = valor % 20
    print('%d nota(s) de R$ 20,00'% nota_20)

    nota_10 = valor // 10
    valor = valor % 10
    print('%d nota(s) de R$ 10,00'% nota_10)

    nota_5 = valor // 5
    valor = valor % 5
    print('%d nota(s) de R$ 5,00'% nota_5)

    nota_2 = valor // 2
    valor = valor % 2
    print('%d nota(s) de R$ 2,00'% nota_2)

    print('%d nota(s) de R$ 1,00'% valor)

main()
