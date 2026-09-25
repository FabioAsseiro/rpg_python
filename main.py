import random
from rich import print

from Event.explorar import explorar
from Event.shop import showShop, creatShop
from Player.player import Player
from Event.combate import combate
from Event.descanso import heal_life


turn = 1
player_list: list[Player] = []
playerAtual = 0

qtd = int(input("Quantos Players vão jogar? "))

while True:
    if qtd <= 1:
        qtd = int(input("Digite um número de Players novamente, no mínimo 2: "))
    else:
        break

for i in range(qtd):
    nome = input(f'Qual nome do Player {i + 1}? ')
    hp = 100
    danobase = 10
    gold = random.randint(15, 30)
    player = Player(nome, hp,danobase, gold)
    player_list.append(player)


loja = creatShop(turn)

while True:

    for i in range(qtd):

        print(
            f'''
            =================================================
                              Turno {turn}
            =================================================
            '''
        )

        playerAtual: Player = player_list[i]

        print(
            f'''
            [bold]Vez do jogador {playerAtual.nome} [/]

            HP: {playerAtual.hp}
            Gold: {playerAtual.gold}
            Danobase: {playerAtual.danobase}
            
            Arma: {playerAtual.arma.nome if playerAtual.arma else "Nenhuma"}
            Armadura: {playerAtual.armadura.nome if playerAtual.armadura else "Nenhuma"}
            Anel: {playerAtual.anel.nome if playerAtual.anel else "Nenhuma"}

            [1] - Atacar
            [2] - Loja
            [3] - Descansar
            [4] - Inventário
            [5] - Explorar
            '''
        )

        while True:

            option = int(input(f"Qual ação do {playerAtual.nome}? "))

            if option == 1:
                combate(playerAtual, player_list, qtd)
                break

            elif option == 2:
                showShop(loja, playerAtual, turn)

            elif option == 3:
                heal_life(playerAtual, turn)
                break

            elif option == 4:
                playerAtual.mostrar_inventario()


            elif option == 5:
                explorar(turn, playerAtual)
                break

            else:
                print("Digite um numero correto")

    for player in player_list:
        if player.hp <= 0:
            print(f"{player.nome} morreu e não está mais jogando")

    player_list = [
        player for player in player_list
        if player.hp > 0
    ]

    qtd = len(player_list)

    if qtd <= 1:
        break
    loja.clear()
    turn += 1
    loja = creatShop(turn)


