# Joguinho simples pelo terminal;
# Objetivo: Achar o tesouro;
# Caminho: Ir para frente ou para tras, pular e bater.



# Criação de personagem
personagem = {
    "nome": input("Nome do seu personagem: "),
    "nivel": 0
}

print ("Esses são os dados do seu personagem nesse inicio: \n", personagem );

# Decisão para iniciar o jogo
inicio_game = input("Podemos iniciar o jogo? Digite 'Sim' para iniciar ou 'Não' para encerrar. \n")

if inicio_game.lower() == "sim":
    print("Maravilha, vamos dar inicio ao jogo! \n");
    start_game = inicio_game;
else:
    print("Espero você numa proxima jornada!");
    start_game = inicio_game;

# Inicio do game

def game_state1():
    print(f"Olá", personagem["nome"], "seja bem vindo a essa breve jornada! \n");
    print("Seu objetivo é conseguir andar até encontrar o tesouro perdido \n")

game_state1()
