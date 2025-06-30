'''
Problema 1013 BeeCrowd
2025/06/25
Luiz.Carlos.Oliveira.Neto
'''
# OBJETIVO : Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.

# VARIAVEIS :  cria as variaveis  para ser usadas mais abaixo
v = input().split()
a = int(v[0])
b = int(v[1])
c = int(v[2])
maior =max(a, b, c)
# MOSTRA NA TELA : Mostra na tela se 'eh Maior'
print('{} eh o maior' .format(maior))