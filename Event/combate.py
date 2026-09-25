import random

from Event.monstro import Monstro
from Event.shop import createItem
from Player.player import Player


def combate(playerAtual: Player, player_list: list[Player], qtd: int):
    # Mostrar os jogadores que são possiveis de ser atacadados pelo o jogador atual.
    for j in range(qtd):
        if player_list[j] != playerAtual:
            print(
                f'[{j}] Atacar jogador {player_list[j].nome}'
            )
    while True:
        alvo = int(input('Qual jogador deseja atacar? '))

        if 0 <= alvo < len(player_list) and player_list[alvo] != playerAtual:
            damage : int = playerAtual.danobase
            shieldAlvo : int = 0

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
        f'{playerAtual.nome} atacou o {player_list[alvo].nome} e tirou {damage}, vida atual é {player_list[alvo].hp}'
    )
    print(
        f'\nA armadura do {player_list[alvo].nome} evitou {shieldAlvo} de dano' if player_list[alvo].armadura is not None else ''
    )

def combateExplorar(playerAtual: Player, monstro: Monstro, turn):

    while True:

        print(f"""
        ================================
                 COMBATE
        ================================

        {playerAtual.nome}
        HP: {playerAtual.hp}

        {monstro.nome}
        HP: {monstro.hp}

        [1] - Atacar
        [2] - Fugir
        """)

        option = int(input("Escolha uma ação: "))

        if option == 1:

            # Dano do jogador
            dano = playerAtual.danobase

            if playerAtual.arma is not None:
                dano += playerAtual.arma.damage

            monstro.hp -= dano

            print(
                f"{playerAtual.nome} atacou {monstro.nome} "
                f"e causou {dano} de dano!"
            )

            # Verifica se o monstro morreu
            if monstro.hp <= 0:
                monstro.hp = 0

                print(f"{monstro.nome} foi derrotado!")

                if random.randint(1, 5) == 5:

                    recompensa = random.choice(["item", "ouro"])

                    if recompensa == "item":
                        drop = createItem(turn)
                        playerAtual.add_item_inventario(drop)

                        print(f"O {playerAtual.nome} recebeu o item: {drop.nome}")

                    else:
                        ouro = random.randint(monstro.nivel, monstro.nivel * 2)
                        playerAtual.addGold(ouro)

                        print(f"O {playerAtual.nome} recebeu a quantidade de ouro: {ouro}")

                return True

            # Ataque do monstro
            dano_monstro = monstro.damage

            playerAtual.hp -= dano_monstro

            print(
                f"{monstro.nome} atacou {playerAtual.nome} "
                f"e causou {dano_monstro} de dano!"
            )

            # Verifica se o jogador morreu
            if playerAtual.hp <= 0:
                playerAtual.hp = 0

                print(f"{playerAtual.nome} foi derrotado!")

                return False

        elif option == 2:

            print(f"{playerAtual.nome} fugiu do combate!")
            return False

        else:
            print("Opção inválida.")