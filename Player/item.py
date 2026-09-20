class Item:
        def __init__(self, nome, value=0, tipo=None, raridade: str = "Comum"):
            self.nome: str = nome
            self.value: int = value
            self.tipo: str = tipo #arma, anel, armadura
            self.raridade: str = raridade

class Armadura(Item):
    def __init__(self, nome, value=0, tipo=None, shield: int = 0, raridade: str = "Comum"):
        super().__init__(nome, value, tipo, raridade)
        self.shield = shield


class Arma(Item):
    def __init__(self, nome, value=0, tipo=None, raridade: str = "Comum", damage: int = 0):
        super().__init__(nome, value, tipo, raridade)
        self.damage = damage

class Anel(Item):
    def __init__(self, nome, value=0, tipo=None, raridade: str = "Comum", agility: int = 0):
        super().__init__(nome, value, tipo, raridade)
        self.agility = agility

