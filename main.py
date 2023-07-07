import os
import sys
import cmd
import time
import random
import textwrap
from map import zonemap, a_escadarias, mapa_escritorio, mapa_cobertura, mapa_terreo, mapas_escadas


# Configuração do jogador
class Player:
    def __init__(self):
        self.HP = 100
        self.STA = 50
        self.MP = 100
        self.location = "escritorio"


player = Player()

perseguidor_status = {
    "HP": 100,
}


# Funções para ações do jogo
def abrir_objeto(objeto):
    if objeto == "porta":
        # Lógica para abrir porta
        pass
    elif objeto == "caixa":
        # Lógica para abrir caixa
        pass
    elif objeto == "armário":
        # Lógica para abrir armário
        pass
    else:
        print("Objeto inválido.")


def inspecionar(objeto):
    if objeto == "local":
        examine_current_location()
    else:
        # Lógica para inspecionar objeto
        pass


def andar(direcao):
    if direcao == "frente":
        # Lógica para andar para frente
        pass
    elif direcao == "trás":
        # Lógica para andar para trás
        pass
    elif direcao == "esquerda":
        # Lógica para andar para a esquerda
        pass
    elif direcao == "direita":
        # Lógica para andar para a direita
        pass
    elif direcao == 'baixo':
        if zonemap[player.location]['locked']:
            print("As escadarias estão trancadas. Você não pode descer para o térreo.")
        else:
            player.location = 'terreo'
            examine_current_location()
    else:
        print("Direção inválida.")


def examine_current_location():
    current_zone = zonemap[player.location]
    print("Você está em", current_zone['zonename'])
    print(current_zone['descriptions'])
    if player.location == 'escadarias':
        if current_zone['solved']:
            print("As correntes foram removidas das portas corta-fogo.")
            print("Opções disponíveis:")
            print("- Examinar: Examinar a área atual")
            print("- Mover-se: Mover-se para outra direção")
            # Outras opções e lógica do jogo
        else:
            print("As portas corta-fogo estão trancadas com grossas correntes.")
            print("Você precisa encontrar uma forma de removê-las para prosseguir.")
            # Outras opções e lógica do jogo
    elif player.location == 'escritorio':
        if mapas_escadas['escadarias']['solved_places']['d4']:
            print("Você pode voltar para as escadarias.")
        else:
            print("Você precisa resolver as escadarias para acessar esta área.")
    elif player.location == 'terreo' or player.location == 'cobertura':
        if zonemap['escadarias']['solved_places']['d4']:
            print("Você pode voltar para as escadarias.")
        else:
            print("Você precisa resolver as escadarias para acessar esta área.")


def start_game():
    print("Você está trabalhando até tarde, precisava ficar até as 22 horas para entregar um projeto importante para a empresa. Quando deu a sua hora, você tentou pegar o elevador para descer ao térreo, mas o mesmo estava desativado. Ao tentar descer as escadas, surpresa, as portas corta-fogo estavam trancadas com grossas correntes.")
    event_ocurred = False
    examine_current_location()

    while True:
        comando = input("Qual será o seu próximo passo? ")

        if comando.startswith("abrir"):
            objeto = comando.split(" ")[1]
            abrir_objeto(objeto)
        elif comando.startswith("inspecionar"):
            objeto = comando.split(" ")[1]
            inspecionar(objeto)
        elif comando.startswith("andar"):
            direcao = comando.split(" ")[1]
            if direcao == "trás" and not event_ocurred:
                print("Você retorna ao escritório, mas percebe que seu celular não está mais em cima da mesa. Alguém o roubou!")
                player.MP -= 10
                print("Seu MP diminuiu em 10 devido ao susto.")
                player.STA -= 5
                print("Sua STA diminuiu em 5% por correr de volta para o escritório.")
                print("Você vê o perseguidor correndo com seu celular nas mãos. Ele está sorrindo maliciosamente e some em uma sala escura.")
                event_ocurred = True
            else:
                andar(direcao)
        elif comando == "ajuda":
            print("=== AJUDA ===")
            print("Comandos disponíveis:")
            print("- abrir <objeto>: Abre um objeto específico")
            print("- inspecionar <objeto>: Inspeciona um objeto específico ou o local")
            print("- andar <direção>: Move-se na direção especificada (frente, trás, esquerda, direita)")
            print("- ajuda: Exibe este menu de ajuda")
            print("- sair: Sai do jogo")
        elif comando == "examinar":
            examine_current_location()
        else:
            print("Comando inválido.")


def title_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("### SCAPER ###")
    print("   - Jogar   ")
    print("   - Ajuda   ")
    print("   - Sair    ")


def title_screen_selections():
    option = input(">")
    if option.lower() == "jogar":
        start_game()
    elif option.lower() == "ajuda":
        print("=== AJUDA ===")
        print("Este é um jogo de aventura em texto. Você controlará o personagem principal e deverá tomar decisões para progredir na história.")
        print("Utilize os seguintes comandos:")
        print("- abrir <objeto>: Abre um objeto específico")
        print("- inspecionar <objeto>: Inspeciona um objeto específico ou o local")
        print("- andar <direção>: Move-se na direção especificada (frente, trás, esquerda, direita)")
        print("- ajuda: Exibe este menu de ajuda")
        print("- sair: Sai do jogo")
    elif option.lower() == "sair":
        sys.exit()
    else:
        print("Comando inválido.")


while True:
    title_screen()
    title_screen_selections()
