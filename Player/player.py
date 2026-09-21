from .item import Item, Arma, Armadura, Anel


class Player:
    def __init__(self, nome: str, hp: int,danobase:int, gold: int):
        self.name = nome
        self.hp = hp
        self.danobase = danobase
        self.agility = 0
        self.level = 1
        self.xp = 0
        self.gold = gold
        self.inventario = []

        # slots
        self.arma: Arma | None = None
        self.anel: Anel | None = None
        self.armadura: Armadura | None = None

    def add_item_inventario(self, item: Item):
        print(f"{item.nome} foi adicionado com sucesso")
        self.inventario.append(item)

    def mostrar_inventario(self):
        if not self.inventario:
            print("Inventário vazio")
            return

        for i, item in enumerate(self.inventario):
            equipado = (
                    item == self.arma
                    or item == self.anel
                    or item == self.armadura
            )

            print(f'[{i}] - {item.nome}{" - EQUIPADO" if equipado else ""}')

        option = input("Qual equipamento quer ver? Use *sair* para sair: ").strip()

        if option.lower() == "sair":
            print(f"{self.name} saiu com sucesso")
        else:
            self.mostrar_item(self.inventario[int(option)])

    def equipar(self, item: Item):
        if item not in self.inventario:
            print(f"{item.nome} não está no inventário")
            return

        if item.tipo == "Arma":
            if self.arma:
                print(f"Desequipando {self.arma.nome}")

            self.arma = item

        elif item.tipo == "Anel":
            if self.anel:
                print(f"Desequipando {self.anel.nome}")

            self.anel = item

        elif item.tipo == "Armadura":
            if self.armadura:
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
        if isinstance(item, Arma):
            atribute = f"Dano: {item.damage}"
        elif isinstance(item, Armadura):
            atribute = f"Armadura: {item.shield}"
        elif isinstance(item, Anel):
            atribute = f"Agility: {item.agility}"
        else:
            atribute = ""

        option = input(f'''
                   ====================================
                               {item.nome}
                   ====================================

                   valor: {item.value}
                   {atribute}
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