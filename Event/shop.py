import random
from rich import print

from Player.item import Arma, Armadura, Anel, Item
from Player.player import Player

armas = [
    "Espada",
    "Faca",
    "Arco",
    "Bastão",
    "Machado",
    "Lança",
    "Adaga",
    "Martelo",
    "Clava",
    "Foice",
    "Katana",
    "Espada Longa",
    "Espada Curta",
    "Montante",
    "Alabarda",
    "Mangual",
    "Maça",
    "Punhal",
    "Arco Longo",
    "Besta",
    "Cajado",
    "Tridente",
    "Machado de Batalha",
    "Martelo de Guerra"
]

armaduras = [
    "Armadura",
    "Escudo",
    "Peitoral",
    "Cota de Malha",
    "Elmo",
    "Capacete",
    "Couraça",
    "Armadura de Batalha",
    "Armadura Pesada",
    "Armadura Leve",
    "Manto",
    "Túnica",
    "Brunea",
    "Grevas",
    "Manoplas",
    "Escudo Redondo",
    "Escudo Torre",
    "Escudo de Batalha"
]

aneis = [
    "Anel",
    "Brinco",
    "Colar",
    "Amuleto",
    "Pingente",
    "Bracelete",
    "Pulseira",
    "Medalhão",
    "Talismã",
    "Broche",
    "Relicário"
]

adjetivos = [
    "Flamejante",
    "Sombrio",
    "Congelante",
    "Elétrico",
    "Sagrado",
    "Amaldiçoado",
    "Dourado",
    "Prateado",
    "Enferrujado",
    "Místico",
    "Arcano",
    "Divino",
    "Infernal",
    "Ancestral",
    "Lendário",
    "Venenoso",
    "Sangrento",
    "Brutal",
    "Feroz",
    "Eterno",
    "Espectral",
    "Celestial",
    "Abissal",
    "Dracônico",
    "Élfico",
    "Anão",
    "Real",
    "Imperial",
    "Perdido",
    "Proibido",
    "de Ferro",
    "de Madeira",
    "de Bronze",
    "de Prata",
    "de Ouro",
    "de Esmeralda",
    "de Rubi",
    "de Safira",
    "de Diamante",
    "de Obsidiana"
]

locais = [
    "do Deserto",
    "da Floresta Escura",
    "do Oceano",
    "do Reino Mágico",
    "das Montanhas",
    "das Cavernas",
    "do Vulcão",
    "do Reino Perdido",
    "da Cidade Antiga",
    "do Castelo Sombrio",
    "das Terras Congeladas",
    "das Terras Áridas",
    "do Pântano",
    "da Ilha Perdida",
    "do Vale Sombrio",
    "da Floresta Encantada",
    "do Reino dos Mortos",
    "das Ruínas Antigas",
    "do Templo Sagrado",
    "da Cidade Dourada",
    "do Abismo",
    "dos Céus",
    "do Inferno",
    "do Submundo",
    "da Terra dos Dragões",
    "do Reino Élfico",
    "das Montanhas de Ferro",
    "do Castelo Real",
    "das Terras Proibidas",
    "do Reino Antigo"
]


def createItem(turn):

    # Define o tipo do item
    tipo = random.choice([
        "arma",
        "armadura",
        "anel"
    ])

    # Define a raridade
    raridade = random.choices(
        ["Comum", "Incomum", "Raro", "Épico", "Lendário"],
        weights=[60, 25, 9, 5, 1]
    )[0]

    # Define o multiplicador da raridade
    multiplicadores = {
        "Comum": 1,
        "Incomum": 1.25,
        "Raro": 1.5,
        "Épico": 2,
        "Lendário": 2.5
    }

    multiplicador = multiplicadores[raridade]

    # Valor base dos itens baseado no turno
    valor_base = random.randint(
        max(1,turn // 2),
        int(turn * 1.75)
    )

    value = int(valor_base * multiplicador)

    # =========================
    # ARMA
    # =========================

    if tipo == "arma":

        nome = random.choice(armas)

        if raridade != "Comum":
            if raridade == "Épico":
                adjetivo = "Épico"
            else:
                adjetivo = random.choice(adjetivos)
            local = random.choice(locais)

            nome = f"{nome} {adjetivo} {local}"

        damage_base = random.randint(
            turn // 2,
            int(turn * 1.75)
        )

        damage = max(1, int(damage_base * multiplicador))

        return Arma(
            nome=nome,
            value=value,
            tipo="Arma",
            raridade=raridade,
            damage=damage
        )

    # =========================
    # ARMADURA
    # =========================

    elif tipo == "armadura":

        nome = random.choice(armaduras)

        if raridade != "Comum":
            if raridade == "Épico":
                adjetivo = "Épico"
            else:
                adjetivo = random.choice(adjetivos)
            local = random.choice(locais)

            nome = f"{nome} {adjetivo} {local}"

        shield_base = random.randint(
            turn // 2,
            int(turn * 1.75)
        )

        shield = max(1,int(shield_base * multiplicador))

        return Armadura(
            nome=nome,
            value=value,
            tipo="Armadura",
            raridade=raridade,
            shield=shield
        )

    # =========================
    # ANEL
    # =========================

    elif tipo == "anel":

        nome = random.choice(aneis)

        if raridade != "Comum":
            if raridade == "Épico":
                adjetivo = "Épico"
            else:
                adjetivo = random.choice(adjetivos)
            local = random.choice(locais)

            nome = f"{nome} {adjetivo} {local}"

        agility_base = random.randint(
            1,
            max(1, turn // 2)
        )
        agility = max(1,int(agility_base * multiplicador))

        return Anel(
            nome=nome,
            value=value,
            tipo="Anel",
            raridade=raridade,
            agility=agility
        )

def creatShop(turn: int):
    loja = []

    for _ in range(3):
        loja.append(createItem(turn))

    return loja

def buyShop(item: Item, playerAtual: Player):

    if playerAtual.gold >= item.value:

        playerAtual.gold -= item.value
        playerAtual.add_item_inventario(item)
        playerAtual.equipar(item)

        print(
            f"O item {item.nome} foi comprado com sucesso!\n"
            f"Seu gold atual é: {playerAtual.gold}"
        )

    else:
        print("Você não tem gold suficiente.")


def showShop(loja: list, playerAtual: Player, turn: int):

    for i, item in enumerate(loja):

        raridade = {
            "Comum": "white",
            "Incomum": "green",
            "Raro": "blue",
            "Épico": "purple",
            "Lendário": "Yellow",
        }

        tipoInfo = ""

        if item.tipo == "Arma":
            tipoInfo = f"{item.damage} de força"

        elif item.tipo == "Armadura":
            tipoInfo = f"{item.shield} de armadura"

        elif item.tipo == "Anel":
            tipoInfo = f"{item.agility} de agilidade"

        print(
            f"[{raridade[item.raridade]}]{i} - [bold]{item.nome}[/] | {tipoInfo} | {item.raridade} | {item.value} ouro | {item.tipo}[/]"
        )

    option = int(
        input("Qual o item que deseja comprar? Digite 4 para sair: ")
    )

    # Sair da loja
    if option == 4:
        return

    # Verifica se o índice escolhido existe
    if 0 <= option < len(loja):

        # Pega o item escolhido pelo jogador
        item_escolhido = loja[option]

        buyShop(item_escolhido, playerAtual)
        loja.pop(option)
        loja.append(createItem(turn))

    else:
        print("Opção inválida.")