from .item import Item


class Player:
    def __init__(self, nome: str, hp: int, gold: int):
        self.name = nome
        self.hp = hp
        self.danobase = 0
        self.agility = 0
        self.level = 1
        self.xp = 0
        self.gold = gold
        self.inventario = []

        # slots
        self.arma: Item | None = None
        self.anel: Item | None = None
        self.armadura: Item | None = None

    def add_item_inventario(self, item: Item):
        print(f"{item.nome} foi adicionado com sucesso")
        self.inventario.append(item)

    def mostrar_inventario(self):
        if not self.inventario:
            print("Inventário vazio")
            return

        for i, item in enumerate(self.inventario):
            equipado = bool
            equipadostr = ""

            if item.tipo == "arma" and self.arma == item:
                equipado = True
                equipadostr = " - EQUIPADO"

            elif item.tipo == "anel" and self.anel == item:
                equipado = True
                equipadostr = " - EQUIPADO"

            elif item.tipo == "armadura" and self.arma == item:
                equipado = True
                equipadostr = " - EQUIPADO"

            print(f"[{i}] - {item.nome}{equipadostr}")

        option = input("Qual equipamento quer ver? Use *sair* para sair: ").strip()

        if option.lower() == "sair":
            print(f"{self.name} saiu com sucesso")
        else:
            self.mostrar_item(self.inventario[int(option)])

    def equipar(self, item: Item):
        if item not in self.inventario:
            print(f"{item.nome} não está no inventário")
            return

        if item.tipo == "arma":
            if self.arma:
                print(f"Desequipando {self.arma.nome}")

            self.arma = item

        elif item.tipo == "anel":
            if self.anel:
                print(f"Desequipando {self.anel.nome}")

            self.anel = item

        elif item.tipo == "armadura":
            if self.arma:
                print(f"Desequipando {self.armadura.nome}")

            self.armadura = item

        print(f"{self.name} equipou o {item.nome} com sucesso")

    def desequipar(self, item: Item):
        if item not in self.inventario:
            print(f"{item.nome} não está no inventário")
            return

        if item.tipo == "arma":
            if self.arma == item:
                self.arma = None
                print(f"{item.nome} foi desequipada com sucesso")
            else:
                print(f"{item.nome} não está equipada")

        elif item.tipo == "anel":
            if self.anel == item:
                self.anel = None
                print(f"{item.nome} foi desequipado com sucesso")
            else:
                print(f"{item.nome} não está equipado")

        elif item.tipo == "armadura":
            if self.armadura == item:
                self.armadura = None
                print(f"{item.nome} foi desequipada com sucesso")
            else:
                print(f"{item.nome} não está equipada")

        else:
            print(f"{item.nome} não pode ser desequipado")

    def mostrar_item(self, item: Item):
        equipado = (
                item == self.arma
                or item == self.anel
                or item == self.armadura
        )
        option = input(f'''
                   ====================================
                               {item.nome}
                   ====================================

                   valor: {item.value}
                   Dano: {item.damage}
                   Agility: {item.agility}
                   Raridade: {item.raridade}
                   Tipo: {item.tipo}

                   {"[0] - Desequipar" if equipado else "[0] - Equipar"}
                   [1] - Voltar
            ''')

        if int(option) == 0:
            if equipado:
                self.desequipar(item)
            else:
                self.equipar(item)