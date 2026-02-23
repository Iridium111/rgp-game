
class Item:
    def __init__(self, name, category):
        self.name = name
        self.category = category


class Weapon(Item):
    def __init__(self, name, damage, category, strength=None, value_strength=None, agility=None, value_agility=None,
                 intellect=None, value_intellect=None):
        super().__init__(name, category)
        self.damage = damage
        self.strength = strength
        self.agility = agility
        self.intellect = intellect
        self.value_strength = value_strength
        self.value_agility = value_agility
        self.value_intellect = value_intellect

    def __repr__(self):
        return (f'{self.category}\n{self.name} Характеристики:\nУрон: {self.damage}\n{self.strength}:{self.value_strength}\n'
                f'{self.agility}:{self.value_agility}\n{self.intellect}:{self.value_intellect}\n')


class Armor(Item):
    def __init__(self, name, category, strength=None, value_strength=None, agility=None, value_agility=None,
                 intellect=None, value_intellect=None):
        super().__init__(name, category)
        self.strength = strength
        self.agility = agility
        self.intellect = intellect
        self.value_strength = value_strength
        self.value_agility = value_agility
        self.value_intellect = value_intellect

    def __repr__(self):
        return (f'{self.category}\n{self.name} Характеристики:\n{self.strength}:{self.value_strength}\n'
                f'{self.agility}:{self.value_agility}\n{self.intellect}:{self.value_intellect}\n')


class Helmet(Armor):
    def __init__(self, name, category, strength=None, value_strength=None, agility=None, value_agility=None,
                 intellect=None, value_intellect=None):
        super().__init__(name, category, strength, value_strength, agility, value_agility, intellect,
                         value_intellect)

    def __repr__(self):
        return (f'{self.category}\n{self.name} Характеристики:\n{self.strength}:{self.value_strength}\n'
                f'{self.agility}:{self.value_agility}\n{self.intellect}:{self.value_intellect}\n')


class Chestplate(Armor):
    def __init__(self, name, category, strength=None, value_strength=None, agility=None, value_agility=None,
                 intellect=None, value_intellect=None):
        super().__init__(name, category, strength, value_strength, agility, value_agility, intellect,
                         value_intellect)

    def __repr__(self):
        return (f'{self.category}\n{self.name} Характеристики:\n{self.strength}:{self.value_strength}\n'
                f'{self.agility}:{self.value_agility}\n{self.intellect}:{self.value_intellect}\n')


class Greaves(Armor):
    def __init__(self, name, category, strength=None, value_strength=None, agility=None, value_agility=None,
                 intellect=None, value_intellect=None):
        super().__init__(name, category, strength, value_strength, agility, value_agility, intellect,
                         value_intellect)

    def __repr__(self):
        return (f'{self.category}\n{self.name} Характеристики:\n{self.strength}:{self.value_strength}\n'
                f'{self.agility}:{self.value_agility}\n{self.intellect}:{self.value_intellect}\n')


class Boots(Armor):
    def __init__(self, name, category, strength=None, value_strength=None, agility=None, value_agility=None,
                 intellect=None, value_intellect=None):
        super().__init__(name, category, strength, value_strength, agility, value_agility, intellect,
                         value_intellect)

    def __repr__(self):
        return (f'{self.category}\n{self.name} Характеристики:\n{self.strength}:{self.value_strength}\n'
                f'{self.agility}:{self.value_agility}\n{self.intellect}:{self.value_intellect}\n')
