class Item:
        def __init__(self, nome, damage=0, value=0, agility: int = 0, tipo=None):
            self.nome: str = nome
            self.damage: int = damage
            self.value: int = value
            self.agility: int = agility
            self.tipo: str = tipo #arma, anel, armadura