import random

from Event.shop import createItem
from Player.item import Item


class Monstro:
   def __init__(self,nome,hp,damage,defesa,nivel,raridade):
    self.nome = nome
    self.hp = hp
    self.damage = damage
    self.defesa = defesa
    self.nivel = nivel
    self.raridade = raridade
    self.drop : Item | None = None


def criarMonstro(turn,PlayerAtual):

    raridade = random.choices(
        ["Comum", "Raro", "Épico", "Chefe"],
        weights=[80, 14, 5, 1]
    )[0]

    multiplicador = {
        "Comum": 1,
        "Raro": 1.5,
        "Épico": 2,
        "Chefe": 3
    }

    if raridade == "Comum":
        nome = random.choice(monstros_comuns)

    elif raridade == "Raro":
        nome = random.choice(monstros_raros)

    elif raridade == "Épico":
        nome = random.choice(monstros_epicos)

    elif raridade == "Chefe":
        nome = random.choice(chefes)

    hp = random.randint(turn, int(turn * multiplicador[raridade]))
    defesa = random.randint(turn, int(turn * multiplicador[raridade]))
    nivel = random.randint(turn, int(turn * multiplicador[raridade]))
    damage = random.randint(turn, int(turn * multiplicador[raridade]))

    drop = None

    return Monstro(nome,hp,damage,defesa,nivel,drop)


monstros_comuns = [
    "Goblin",
    "Slime",
    "Rocha",
    "Lobo",
    "Morcego",
    "Aranha Gigante",
    "Javali Selvagem",
    "Cobra",
    "Esqueleto",
    "Zumbi",
    "Orc",
    "Serpente"
]

monstros_raros = [
    "Troll",
    "Urso",
    "Cobra Gigante",
    "Lobisomem",
    "Golem de Pedra",
    "Harpia",
    "Centauro",
    "Bruxa",
    "Vampiro",
    "Múmia",
    "Cavaleiro",
    "Golem"
]


monstros_epicos = [
    "Golem de Ferro",
    "Elemental de Fogo",
    "Elemental de Gelo",
    "Elemental de Terra",
    "Elemental de Ar",
    "Necromante",
    "Demônio",
    "Fantasma",
    "Espectro",
    "Minotauro",
    "Quimera",
    "Grifo",
    "Cavaleiro Negro",
    "Cavaleiro Espectral"
]


chefes = [
    "Rei Goblin",
    "Rei Orc",
    "Rei Esqueleto",
    "Hidra",
    "Kraken",
    "Serpente Marinha",
    "Dragão de Gelo",
    "Dragão de Fogo",
    "Dragão Sombrio",
    "Senhor Demônio"
]