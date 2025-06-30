'''
Problema 1050 - BeeCrowd
2025/05/27
Luiz Carlos Oliveira Neto
'''
# Objetivo: Ver o destino do passageiro de acordo com o numeros
# Define o destino do individo
Destination = int(input())
# Se o destino for 61 sera Brasilia
if (Destination == 61):
    print('Brasilia')
# Se o destino for 71 sera Salvador
elif (Destination == 71):
    print("Salvador")
# Se o destino for 11 sera São Paulo
elif (Destination == 11):
    print('Sao Paulo')
# Se o destino for 21 sera Rio de Janeiro
elif (Destination == 21):
    print('Rio de Janeiro')
# Se o destino for 32 sera Juiz de Fora
elif (Destination == 32):
    print('Juiz de Fora')
# Se o destino for 19 sera Campinas
elif (Destination == 19):
    print('Campinas')
# Se o destino for 27 sera Vitoria
elif (Destination == 27):
    print('Vitoria')
# Se o destino for 31 sera Belo Horizonte
elif (Destination == 31):
    print('Belo Horizonte')
else:
    print('DDD nao cadastrado')