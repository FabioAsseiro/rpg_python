import random

from Player.player import Player


def heal_life(playerAtual: Player, turn: int):
    vida_antiga = playerAtual.hp

    if turn > 10:
        heal_Life = random.randint(10, int(turn * 1.5))
    else:
        heal_Life = 10

    playerAtual.hp += heal_Life

    print(f"O jogador {playerAtual.nome} recuperou {heal_Life} de vida")
    print(f"Vida Antiga: {vida_antiga}")
    print(f"Vida Atual: {playerAtual.hp}")
