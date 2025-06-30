'''
Problema 1035 BeeCrowd
2025/06/25
Luiz.Carlos.Oliveira.Neto
'''
# Objetivo : #Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

# Ceia uma variavel

a, b, c, d = map(int, input().split())

# cria if para a resolução
'''if b>c and d>a and c+d > a + b and c >= 0 and d >= 0 and a%2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')'''

todosCorretos = False

if b > c:
    if d > a:
        if c + d > a + b:
            if c >= 0 and d >= 0:
                if a%2 == 0:
                    print('Valores aceitos')

                    todosCorretos = True

if not todosCorretos:
    print('Valores nao aceitos')
                