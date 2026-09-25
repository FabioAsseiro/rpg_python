from Event.combate import combateExplorar
from Event.monstro import criarMonstro


def explorar(turn, playerAtual):
    monstro = criarMonstro(turn, playerAtual)
    combateExplorar(playerAtual, monstro, turn)


eventos = [
    "combate",
    "npc",
    "bau",
    "Evento aleatorio"
]