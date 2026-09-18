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
            break
        else:
            print('Coloque um numero valido')
    print(
        f'{playerAtual.name} atacou o/a {player_list[alvo].name}'
    )