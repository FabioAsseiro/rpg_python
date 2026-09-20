import random

from Player.player import Player


def combate(playerAtual: Player, player_list: list[Player], qtd: int):
    # Mostrar os jogadores que são possiveis de ser atacadados pelo o jogador atual.
    for j in range(qtd):
        if player_list[j] != playerAtual:
            print(
                f'[{j}] Atacar jogador {player_list[j].name}'
            )
    while True:
        alvo = int(input('Qual jogador deseja atacar? '))

        if 0 <= alvo < len(player_list) and player_list[alvo] != playerAtual:
            damage : int = playerAtual.danobase
            shieldAlvo : int = 0

            if playerAtual.anel is not None:
                damage += playerAtual.anel.damage

            if playerAtual.arma is not None:
                damage += playerAtual.arma.damage

            if player_list[alvo].armadura is not None:
                shieldAlvo = round(player_list[alvo].armadura.shield * random.uniform(0.3, 1))
                damage -= shieldAlvo

            player_list[alvo].hp -= damage
            break
        else:
            print('Coloque um numero valido')
    print(
        f'{playerAtual.name} atacou o {player_list[alvo].name} e tirou {damage}, vida atual é {player_list[alvo].hp}'
        f'\nA armadura do {player_list[alvo].name} evitou {shieldAlvo} de dano' if player_list[alvo].armadura is not None else ''
    )