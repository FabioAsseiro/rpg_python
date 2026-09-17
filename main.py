import random


class Player:
    name = ""
    hp = 0
    weapon = ""
    armor = ""
    level = 1
    xp = 0
    gold = 0

turn = 1
player_list: list[Player] = []
playerAtual = ''
qtd = int(input("Quantos Players vão jogar? "))

for i in range(qtd):
    player = Player()
    player.name = input(f'Qual nome do Player {i+1}? ')
    player.hp = 100
    player.gold = random.randint(15, 30)

    player_list.append(player)

for i in range(qtd):
    print(
    f'''
    =================================================
                      Turno {turn}
    =================================================
    '''
    )
    playerAtual: Player = player_list[i]

    print(f'''
    Vez do jogador {playerAtual.name}

    [1] - Atacar
    [2] - Loja
    [3] - Descansar
    ''')

    option = int(input(f"Qual ação do {playerAtual.name}? "))

    if option == 1:

        # Mostrar os jogadores que são possiveis de ser atacadados pelo o jogador atual.
        for j in range(qtd):
            if player_list[j] != playerAtual:
                print(
                    f'[{j}] Atacar jogador {player_list[j].name}'
                )
        while True:
            alvo = int(input('Qual jogador deseja atacar? '))

            if 0 <= alvo < len(player_list) and player_list[alvo] != playerAtual:
                break
            else:
                print('Coloque um numero valido')
        print(
            f'{playerAtual.name} atacou o/a {player_list[alvo].name}'
        )