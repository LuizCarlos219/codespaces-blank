'''
Problema 1037 - BeeCrowd
2025/05/21
Luiz Carlos Oliveira Neto
'''
# Objetivo: Ler o valor e informar em qual dos intervalos o valor esta
 
# Ler 1 valor == Tipo float
Valor = float(input())

#  Testa o valor maior que 0
if (Valor >= 0):
 #  Testa se o valor e menor ou iqual a 25
 if (Valor <= 25):
  # Mostrar a msg == Intervalo [0.25]
  print('Intervalo [0,25]')
  # Testa o valor 50
 elif (Valor <= 50):
   # mostrar a msg == Intervalo (25,70]
  print('Intervalo (25,50]')
  #Testa o valor 75
 elif (Valor <= 75): 
  #Mostrar a msg == intervalo (75,100]
  print('Intervalo (50,75]')
  #Testa o valor 100
 elif (Valor <= 100): 
  print('Intervalo (75,100]')
  #Caso o teste retorne falso  == Valor > 100
 else: 
  #Mostrar a msg == Fora de intervalo
  print('Fora de intervalo')
  # Caso o primeiro teste retorme False == Valor < 0
else:
  #Mostrar a msg == Fora de intervalo
  print('Fora de intervalo')