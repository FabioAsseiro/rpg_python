from .item import Item

class Player:
    def __init__(self, nome: str,hp: int, gold: int):
        self.name = nome
        self.hp = hp
        self.danobase = 0
        self.agility = 0
        self.level = 1
        self.xp = 0
        self.gold = gold
        self.inventario = []


        #slots

        self.arma = None
        self.anel = None

    def add_item_inventario(self, item: Item):
        print(f"{item.nome} foi adicionado com sucesso")
        self.inventario.append(item)

    def mostrar_inventario(self):
        if not self.inventario:
            print("Inventário vazio")
            return
        for item in self.inventario:
            print(f"[{item}] - {item.nome}")

    def equipar(self, item: Item):
        if item not in self.inventario:
            print(f"{item.name} Não está no inventario")
            return
        if item.tipo == "arma":
            if self.arma:
                print(f"Desequipando {item.name}")
                self.arma = item
        if item.tipo == "anel":
            if self.anel:
                print(f"Desequipando {item.name}")
                self.anel = item
        print(f"{self.name} equipou o {item.nome} com sucesso")