import os
import random 
from colorama import Fore, Back, Style

# Inicializa variáveis de controle do jogo
jogarNovamente = "s" # Variável para controlar se o jogador quer jogar novamente
jogadas = 0 # Contador de jogadas
quemJoga = 2 # Variável que determina quem joga: 1 para CPU, 2 para jogador
maxJogadas = 9 # Número máximo de jogadas permitidas
vit = "n" # Variável para verificar se houve vitória ("n" significa que ainda não houve vitória)
velha = [ # Matriz que representa o tabuleiro do jogo da velha
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Função que desenha a tela do jogo
def tela():
    global velha
    global jogadas
    os.system("cls" if os.name == "nt" else "clear") # Limpa a tela dependendo do sistema operacional
    print("    0   1   2") # Exibe a numeração das colunas
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2]) 
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("   -----------")
    print("Jogadas: " + Fore.MAGENTA + str(jogadas) + Fore.RESET) # Exibe o número de jogadas realizadas

# Função que permite o jogador fazer uma jogada
def jogadorJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas
    if quemJoga == 2 and jogadas < maxJogadas: # Verifica se é a vez do jogador e se ainda há jogadas disponíveis
        l = int(input("Linha..: ")) # Recebe a linha da jogada
        c = int(input("Coluna..: ")) # Recebe a coluna da jogada
        try: 
            while velha[l][c] != " ": # Verifica se a posição já está ocupada
                l = int(input("Linha..: "))
                c = int(input("Coluna..: "))
            velha[l][c] = "X" # Marca a jogada do jogador com "X"
            quemJoga = 1 # Passa a vez para a CPU
            jogadas += 1 # Incrementa o contador de jogadas
        except: 
            print("Jogada inválida, tente novamente") # Mensagem de erro para entradas inválidas
            os.system("pause") # Pausa o jogo para o jogador ver a mensagem

# Função que permite a CPU fazer uma jogada
def cpuJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas
    if quemJoga == 1 and jogadas < maxJogadas: # Verifica se é a vez da CPU e se ainda há jogadas disponíveis
        l = random.randrange(0, 3) # Gera uma linha aleatória
        c = random.randrange(0, 3) # Gera uma coluna aleatória
        while velha[l][c] != " ": # Verifica se a posição já está ocupada
            l = random.randrange(0, 3)
            c = random.randrange(0, 3) 
        velha[l][c] = "O" # Marca a jogada da CPU com "O"
        jogadas += 1 # Incrementa o contador de jogadas
        quemJoga = 2 # Passa a vez para o jogador

# Função que verifica se houve uma vitória no jogo
def verificarVitoria():
    global velha
    vitoria = "n" # Inicialmente, não há vitória
    simbolos = ["X", "O"] # Símbolos dos jogadores (X para jogador e O para CPU)
    
    # Verifica linhas, colunas e diagonais para encontrar uma vitória
    for s in simbolos: 
        vitoria = "n"
        il = ic = 0
        # Verifica as linhas
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if velha[il][ic] == s:
                    soma += 1
                ic += 1
            if soma == 3:
                vitoria = s # Há vitória se uma linha completa for do mesmo símbolo
                break 
            il += 1
        if vitoria != "n":
            break 
        il = ic = 0
        # Verifica as colunas
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if velha[il][ic] == s:
                    soma += 1
                il += 1
            if soma == 3:
                vitoria = s # Há vitória se uma coluna completa for do mesmo símbolo
                break 
            ic += 1
        if vitoria != "n":
            break 

        # Verifica a diagonal principal
        soma = 0
        idiag = 0
        while idiag < 3:
            if velha[idiag][idiag] == s:
                soma += 1
            idiag += 1
        if soma == 3:
            vitoria = s # Há vitória se a diagonal principal for do mesmo símbolo
            break

        # Verifica a diagonal secundária
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagc >= 0:
            if velha[idiagl][idiagc] == s:
                soma += 1
            idiagl += 1
            idiagc -= 1
        if soma == 3:
            vitoria = s # Há vitória se a diagonal secundária for do mesmo símbolo
            break
    return vitoria

# Função que reinicia o jogo para uma nova partida
def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    jogadas = 0 # Reseta o número de jogadas
    quemJoga = 2 # Define que o jogador começa
    maxJogadas = 9 # Reseta o número máximo de jogadas
    vit = "n" # Reseta a vitória
    velha = [ # Reseta o tabuleiro
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

# Loop principal do jogo
while jogarNovamente == "s":
    while True: 
        tela() # Exibe a tela do jogo
        jogadorJoga() # Chama a função para o jogador jogar
        cpuJoga() # Chama a função para a CPU jogar
        tela() # Exibe a tela do jogo após cada jogada
        vit = verificarVitoria() # Verifica se houve vitória
        if vit != "n" or jogadas >= maxJogadas: # Sai do loop se houver vitória ou se o número máximo de jogadas for atingido
            break

    print(Fore.MAGENTA + "Fim de jogo" + Fore.RESET) # Mensagem de fim de jogo
    if vit == "X" or vit == "O":
        print("Resultado: Jogador " + vit + " venceu") # Exibe o vencedor
    else:
        print("Resultado: Empate") # Exibe mensagem de empate
    jogarNovamente = input(Fore.LIGHTMAGENTA_EX + "Jogar novamente? [s/n]: " + Fore.RESET) # Pergunta se o jogador quer jogar novamente
    redefinir() # Reseta o jogo para uma nova partida
