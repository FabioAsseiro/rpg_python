import random

from Player.item import Item
from Player.player import Player
from Event.combate import combate
from Event.descanso import heal_Life


turn = 100
player_list: list[Player] = []
playerAtual = 0

qtd = int(input("Quantos Players vão jogar? "))

while True:
    if qtd <= 1:
        qtd = int(input("Digite um número de Players novamente, no mínimo 2: "))
    else:
        break

for i in range(qtd):
    name = input(f'Qual nome do Player {i + 1}? ')
    hp = 100
    gold = random.randint(15, 30)
    player = Player(name, hp, gold)
    player_list.append(player)

# Teste para adicionar a arma
espada = Item("Espada do jogador", 15, 10,0, "Espada")
faca = Item("Faca do jogador", 15, 10,0, "Faca")
anel = Item("Anel do jogador", 0, 10,10,"Anel")
player_list[0].add_item_inventario(espada)
player_list[0].equipar(espada)
player_list[0].add_item_inventario(faca)
player_list[0].add_item_inventario(anel)
player_list[0].equipar(faca)


def mostrar_inventario(i):
    inventario = player_list[i].mostrar_inventario()
    print(inventario)

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
            Vez do jogador {playerAtual.name} 

            HP: {playerAtual.hp}
            Gold: {playerAtual.gold}

            [1] - Atacar
            [2] - Loja
            [3] - Descansar
            [4] - Inventário
            [5] - Explorar
            '''
        )

        while True:

            option = int(input(f"Qual ação do {playerAtual.name}? "))

            if option == 1:
                combate(playerAtual, player_list, qtd)
                break

            elif option == 2:
                print('Mercado')
                break

            elif option == 3:
                heal_Life(playerAtual, turn)
                break

            elif option == 4:
                mostrar_inventario(i)
                break

            elif option == 5:
                print('Explorar')
                break

            else:
                print("Digite um numero correto")

    turn += 1


