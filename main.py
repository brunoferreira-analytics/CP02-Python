# Jogo da Velha em Python

#Colaboradores:
# Bruno Henrique Ferreira Ambrosio (RM: 571218)
# Adalberto Alves Cruz (RM: 574115)
# Tiago Thomaz Cesaro (RM: 569374)
# Gustavo da Silva Nascimento (RM: 570821)

#Função mostrar o tabuleiro na tela.
def eixibir_tabuleiro(tabuleiro):
   print()

   print("    1   2   3" )

   # Repete 3 vezes:
   for i in range(3):
      
      #Mostra os 3 números.
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
