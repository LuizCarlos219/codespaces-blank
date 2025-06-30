'''
Problema 1015 BeeCrowd
2025/0616
Luiz.Carlos.Oliveira.Neto
'''
# Objetivo:Calcular a distancia entre dois planos em um plano cartesiano, a partir das coordenadas X e Y desses pontos.
#Receber a entrada com os valores correspondentes aos pontos
p1=input().split()
p2=input().split()
#Converter as entradas em valores do tipo float.
x1=float(p1[0])
y1=float(p1[1])
x2=float(p2[0])
y2=float(p2[1])
#Calcular a distancia com base na fórmula.
p1=(x2-x1)**2
p2=(y2-y1)**2
distancia = (p1+p2)**0.5
#Mostrar o resultado com 4 casas decimais.
print(f'{distancia:.4f}')