'''
Projeto 2%Bimestre
Data: 2025.07.02
Autor: Luiz.Carlos.Oliveira.Neto
'''

# objetivo: Um jogo de Pedregulho, Papel e Tesoura com giria brasileira.

import random  # Importa a biblioteca para usar escolhas aleatórias

# Tipos de dados e Variáveis
opcoes = ["pedregulho", "sulfite", "cortador"]  # Lista com as opções possíveis
pontos_jogador = 0  # Contador de pontos do jogador
pontos_computador = 0  # Contador de pontos do computador

# Sub-rotinas (Funções)
def jogada_Bot():
    # Escolhe aleatoriamente uma opção para o computador
    return random.choice(opcoes)

def decidir_vencedor(jogador, Bot):
    # Verifica quem ganhou com base nas regras do jogo
    if jogador == Bot:
        return "empate"
    elif (jogador == "pedregulho" and Bot == "cortador") or \
         (jogador == "sulfite" and Bot == "pedregulho") or \
         (jogador == "cortador" and Bot == "sulfite"):
        return "jogador"
    else:
        return "Bot"

# Função principal do jogo
def jogar():
    global pontos_jogador, pontos_computador  # Permite alterar as variáveis globais
    while True:  #  Estrutura de repetição - enquanto o jogador quiser jogar
        #  Entrada de dados com validação
        jogador = input("Escolha pedregulho, sulfite ou cortador: ").lower()  # Converte para minúsculas
        if jogador not in opcoes:
            print("Ih Zé errou. Tente novamente.")
            continue  # Volta para o início do loop
        
        # Computador faz a jogada
        Bot = jogada_Bot()
        
        #  Saída de dados
        print(f"\nVocê jogou: {jogador}")
        print(f"Computador jogou: {Bot}")
        
        #  Estrutura de decisão
        vencedor = decidir_vencedor(jogador, Bot)
        if vencedor == "empate":
            print("Ih empate Zé!")
        elif vencedor == "jogador":
            print("Você venceu Zé!")
            pontos_jogador += 1  # Adiciona ponto ao jogador
        else:
            print("O Bot venceu!")
            pontos_computador += 1  # Adiciona ponto ao computador
        
        # Mostra o placar atualizado
        print(f"\nPlacar - Você: {pontos_jogador} | Bot: {pontos_computador}")
        
        # Pergunta se o jogador quer continuar
        continuar = input("\nVai jogar de novo Zé? (s/n): ").lower()
        if continuar != 's':
            print("Valeu por jogar Zé!")
            break  # Sai do loop e termina o jogo

# Inicia o jogo
jogar()