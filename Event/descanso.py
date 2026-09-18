import random

from Player.player import Player


def heal_Life(playerAtual: Player, turn: int):
    if turn > 10:
        heal_Life=random.randint(10, int((turn * 1.5 )))
    else:
        heal_Life = 10

    print(f"O jogador {playerAtual.name} recuperou {heal_Life} de vida")
    print(f"Vida Antiga: {playerAtual.hp}")
    print(f"Vida Atual: {(playerAtual.hp + heal_Life)}")
