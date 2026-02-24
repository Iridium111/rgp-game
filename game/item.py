
class Item:
    """Создание оружия и брони для героя."""

    def __init__(self, name, slot, stats=None):
        self.name = name
        self.slot = slot
        self.stats = stats or {}


class Weapon(Item):
    def __init__(self, name, slot, damage, stats=None):
        super().__init__(name, slot, stats)
        self.damage = damage

    def __repr__(self):
        return f'{self.name}\nУрон: {self.damage}\nАтрибуты:\n{self.stats}'


class Armor(Item):
    def __init__(self, name, slot, stats=None):
        super().__init__(name, slot, stats)

    def __repr__(self):
        return f'Броня: {self.slot}\n{self.name}\nАтрибуты:\n{self.stats}'



