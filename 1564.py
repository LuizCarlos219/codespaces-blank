'''
Problema 1759 - BeeCrowd
2025.06.26
Luiz.Carlos.Oliveira.Neto
'''

# Objetivo: O Brasil é o país sede da copa esse ano. Porém, há muitas pessoas protestando contra o governo. Em redes sociais é possível ver pessoas afirmando que não vai ter copa devido aos protestos.Mas esses rumores de que não haverá copa são totalmente falsos, a presidente Dilma Roussef já avisou: vai ter copa sim, e se reclamar vai ter duas!

import sys  # Importa sys para ler entrada até o EOF

# Percorre cada linha da entrada padrão até o fim do arquivo
for linha in sys.stdin:
    # Remove espaços em branco e converte a linha para inteiro
    N = int(linha.strip())
    
    # Se N for 0, imprime "vai ter copa!"
    if N == 0:
        print("vai ter copa!")
    else:
        # Se N for maior que 0, imprime "vai ter duas!"
        print("vai ter duas!")
