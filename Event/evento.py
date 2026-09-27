import random

from Event.shop import createItem
from Player.player import Player


def evento_gold(self: Player):
    gold = random.randint(35, 70)
    self.gold += gold

    print(f"O {self.nome} ganhou {gold} de Gold!")


def evento_xp(self: Player):
    xp = random.randint(1, 100)
    self.xp += xp
    self.up_lvl()
    print(f"O {self.nome} ganhou {xp} de XP!")


def evento_arma(turn,self: Player):
    item = createItem(turn, "Épico")

    self.add_item_inventario(item)
    print(f"O {self.nome} ganhou {item.nome}! ")
