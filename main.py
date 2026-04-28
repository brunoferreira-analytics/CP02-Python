# Jogo da Velha em Python

#Colaboradores:
# Bruno Henrique Ferreira Ambrosio (RM: 571218)
# Adalberto Alves Cruz (RM: 574115)
# Tiago Thomaz Cesaro (RM: 569374)
# Gustavo da Silva Nascimento (RM: 570821)

#Função mostrar o tabuleiro na tela.
def exibir_tabuleiro(tabuleiro):
   print()

   print("    1   2   3" )

   # Repete 3 vezes:
   for i in range(3):
      
      #Mostra os 3 números, (i+1) é para começar do 1 e não do zero.
      print(i + 1, " ", tabuleiro[i][0], "|", tabuleiro[i][1], "|", tabuleiro [i][2])

      #Exibir a separação do tabuleiro.
      if i < 2:
         print("   ---+---+---")

#Função verufucar se algum jogador venceu:
def verificar_vencedor(tabuleiro, jogador):
   
   #Verifica as 3 linhas do tabuleiro.
    for i in range(3):
      
      #Se as 3 linhas forem iguais retorna o jogador vencedor.
      if tabuleiro[i][0] == jogador and tabuleiro [i][1] == jogador and tabuleiro[i][2] == jogador:
         return True #Retorna o jogador ganhador.
      
    #Verifica as 3 colunas do tabuleiro:
    for i in range(3):
      
      #Se as 3 linhas da colunas forem igauis retorna o jogador vencedor.
      if tabuleiro[0][i] == jogador and tabuleiro [1][i] == jogador and tabuleiro [2][i] == jogador:
         return True #Retorna o jogador ganhador.
    
    #Verificar a digonal A
    if tabuleiro[0][0] == jogador and tabuleiro [1][1] == jogador and tabuleiro [2][2] == jogador:
       return True # Retorna o jogador ganhador.
    
    #Verifica a diagonal B
    if tabuleiro [0][2] == jogador and tabuleiro [1][1] == jogador and tabuleiro [2][0] == jogador:
       return True #Retorna o jogador ganhador. 
    
    return False # Se não encontrou vitória, cotinua o jogo.

def verificar_empate(tabuleiro):

    #Percorre as linhas do tabuleiro.
    for linha in range(3):
       
        #Percorre as colunas do tabuleiro.
        for coluna in range(3):
           
           #Se encontrar vazio, continua o jogo.
           if tabuleiro[linha][coluna] == " ":
              return False #Ainda existe jogada possível.
           
    return True #Se não encontrou espaço vazio, o jogo empatou.


# Função responsável por verificar se a jogada é válida.
def jogada_valida(tabuleiro, linha, coluna):

    # Jogada fora do tabuleiro. 
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        return False  # Jogada inválida.

    # Vaga preenchida.
    if tabuleiro[linha][coluna] != " ":
        return False  # Jogada inválida.

    return True  # Se a jogada for válida, retorna True.


# Função principal do jogo.
def jogar():

    # Cria o tabuleiro vazio com 3 linhas e 3 colunas.
    tabuleiro = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    jogador_atual = "X"  # Define que o jogador "X" começa.

    # Mensagens iniciais do jogo.
    print("=== JOGO DA VELHA ===")
    print("Jogador 1: X")
    print("Jogador 2: O")
    print("Digite linha e coluna de 1 a 3.")

    # Loop principal do jogo.
    while True:

        # Mostra o tabuleiro atualizado.
        exibir_tabuleiro(tabuleiro)

        # Mostra qual jogador deve jogar.
        print("Vez do jogador", jogador_atual)

        # Recebe a linha e a coluna digitadas pelo usuário.
        linha_input = input("Digite a linha: ")
        coluna_input = input("Digite a coluna: ")
    
        # Verifica se a linha digitada é diferente de 1, 2 e 3.
        if linha_input != "1" and linha_input != "2" and linha_input != "3":
            print("Linha inválida! Digite apenas 1, 2 ou 3.")
            continue  # Volta para o início do while.

        # Verifica se a coluna digitada é diferente de 1, 2 e 3.
        if coluna_input != "1" and coluna_input != "2" and coluna_input != "3":
            print("Coluna inválida! Digite apenas 1, 2 ou 3.")
            continue  # Volta para o início do while.

        # Converte a linha para número e subtrai 1 por causa do índice 0, 1, 2. 
        linha = int(linha_input) - 1

        # Converte a coluna para número e subtrai 1 por causa do 0, 1, 2.
        coluna = int(coluna_input) - 1

        # Verifica se a jogada é válida.
        if jogada_valida(tabuleiro, linha, coluna):

            # Marca a jogada no tabuleiro.
            tabuleiro[linha][coluna] = jogador_atual

        else:

            # Mensagem caso a posição já esteja ocupada.
            print("Jogada inválida! Essa posição já está ocupada.")
            continue  # Volta para o início do while.

        # Verifica se o jogador atual venceu.
        if verificar_vencedor(tabuleiro, jogador_atual):

            # Mostra o tabuleiro final.
            exibir_tabuleiro(tabuleiro)

            # Mostra mensagem de vitória.
            print("Parabéns! O jogador", jogador_atual, "venceu!")

            break  # Encerra o loop e termina o jogo.

        # Verifica se o jogo empatou. 
        #Gustavo Fez parte.
        if verificar_empate(tabuleiro):

            # Mostra o tabuleiro final.
            exibir_tabuleiro(tabuleiro)

            # Mostra mensagem de empate.
            print("O jogo terminou em empate!")

            break  # Encerra o loop e termina o jogo.

        # Alterna o jogador.
        if jogador_atual == "X":
            jogador_atual = "O"  # Se era X, muda para O.
        else:
            jogador_atual = "X"  # Se era O, muda para X.


# Chama a função principal e inicia o jogo.
jogar()
