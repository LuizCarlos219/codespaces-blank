'''
Projeto: Game  Par ou Impar - V.1.0
2025.06.24
Luiz.Caros
'''

# OBJETIVO: Desenvolver um jogo onde o Jogador escolhe Par ou Impar e faz sua Jogada, o PC sorteia um Número entre 1 e 10 e soma com a Jogada do Jogador, se o resultado for Par eo Jogador escolheu Par, ele ganha, se for Impar e o Jogador escolheu Impar, ele ganha, caso contrário o PC ganha,

# BIBLIOTECAS:
from modules import limpaTela, mostraCabecalho, mostraMenu,getValue, validaValue, sortNum, playAgain
# CONSTANTES:
limite = 10
# VARIÁVEIS:

# LISTAS:
msgsCab = ['JOGO DO PAR OU IMPAR','Feito por Luiz.Carlos']
msgsMenu = ['Escolha:','[0] para Par,', '[1] para Impar']
# FUNÇÃO PRINCIPAL DO JOGO
def playGame():
    global escolha, msg, msgsCab, msgsMenu
    limpaTela()
    mostraCabecalho(msgsCab)
    mostraMenu(msgsMenu)
    msg = '-> Sua escolha:'
    escolha = getValue(msg)
    opcoes = ['0', '1']
    while not validaValue(escolha, opcoes):
        escolha = getValue(msg)
    msg = '-> Sua Jogada: '
    userJogada = getValue(msg)
    while not userJogada.isdigit():
        userJogada = getValue(msg)
    userJogada =  int(userJogada)
    pcJogada= sortNum(limite)
    result = userJogada + pcJogada
    if (result%2 == 0) and escolha == '0':
        ganhador = 'Jogador'
    elif (result%2 != 0) and escolha == '1':
        ganhador = 'Jogador'
    else:
        ganhador = 'PC'
    MSGS = [f'PC Jogou: {pcJogada}', f'Jogador Jogou: {userJogada}',f'Resultado: {result}',f'Ganhador: {ganhador}']
    mostraCabecalho(MSGS) 
    if playAgain():
        playGame()
    else:
        mostraCabecalho(['Obrigado por jogar!', 'Até a próxima'])

# CÓDIGO PRINCIPAL
playGame()