
class Weapon:
    def __init__(self, name, damage, category):
        self.name = name
        self.damage = damage
        self.category = category


class Characteristic:
    def __init__(self, mana, stamina, hero):    #hero - принимает характеристики от своего объекта
        self.mana = mana
        self.stamina = stamina
        self._hero = hero



class Armor:
    def __init__(self, name, category, strength=None, value_strength=None, agility=None, value_agility=None,
                 intellect=None, value_intellect=None):
        self.name = name
        self.category = category
        self.strength = strength
        self.agility = agility
        self.intellect = intellect
        self.value_strength = value_strength
        self.value_agility = value_agility
        self.value_intellect = value_intellect


class Helmet(Armor):
    def __init__(self, name, category, strength=None, value_strength=None, agility=None, value_agility=None,
                 intellect=None, value_intellect=None):
        super().__init__(name, category, strength, value_strength, agility, value_agility, intellect,
                         value_intellect)

    def __repr__(self):
        return (f'{self.category} {self.name} Характеристики:\n{self.strength}:{self.value_strength}\n'
                f'{self.agility}:{self.value_agility}\n{self.intellect}:{self.value_intellect}\n')


class Chestplate(Armor):
    def __init__(self, name, category, strength=None, value_strength=None, agility=None, value_agility=None,
                 intellect=None, value_intellect=None):
        super().__init__(name, category, strength, value_strength, agility, value_agility, intellect,
                         value_intellect)

    def __repr__(self):
        return (f'{self.category} {self.name} Характеристики:\n{self.strength}:{self.value_strength}\n'
                f'{self.agility}:{self.value_agility}\n{self.intellect}:{self.value_intellect}\n')


class Greaves(Armor):
    def __init__(self, name, category, strength=None, value_strength=None, agility=None, value_agility=None,
                 intellect=None, value_intellect=None):
        super().__init__(name, category, strength, value_strength, agility, value_agility, intellect,
                         value_intellect)

    def __repr__(self):
        return (f'{self.category} {self.name} Характеристики:\n{self.strength}:{self.value_strength}\n'
                f'{self.agility}:{self.value_agility}\n{self.intellect}{self.value_intellect}\n')


class Boots(Armor):
    def __init__(self, name, category, strength=None, value_strength=None, agility=None, value_agility=None,
                 intellect=None, value_intellect=None):
        super().__init__(name, category, strength, value_strength, agility, value_agility, intellect,
                         value_intellect)

    def __repr__(self):
        return (f'{self.category} {self.name} Характеристики:\n{self.strength}:{self.value_strength}\n'
                f'{self.agility}:{self.value_agility}\n{self.intellect}:{self.value_intellect}\n')


class Inventory:
    def __init__(self):
        self.slots_category = {}
        self.slots_items = {}

    def add_in_inventory(self, item):
        """Добавление предметов в инвентарь"""
        # Сохраняем по имени
        self.slots_items[item.name] = item

        # Сохраняем по категориям
        if item.category not in self.slots_category:
            self.slots_category[item.category] = {}     # создаем словарь для этой категории
        self.slots_category[item.category][item.name] = item    # кладем предмет в свою категорию

class Hero:
    def __init__(self, name, weapon):
        self._name = name
        self._characteristic = Characteristic(100, 100, self)   #self - для передачи характеристик в Characteristic
        self._weapon = weapon
        self.BASE_HEALTH = 100
        self.BASE_MANA = 100
        self.BASE_STAMINA = 100
        self.slots_armor = {
            'Шлем': None,
            'Нагрудник': None,
            'Поножи': None,
            'Ботинки': None,
        }
        self.amount_strength = 0
        self.health = 0
        self.amount_intellect = 0
        self.mana = 0
        self.amount_agility = 0
        self.stamina = 0

    def equip_armor(self, inventory, key, name_thing):
        """Одевание брони"""
        if self.slots_armor[key]:
            print(f'Слот занят.')

        else:
            if key in inventory.slots_category:
                item = inventory.slots_category[key][name_thing]
                self.slots_armor[key] = item

            else:
                print(f'Нема такова')

    def calculation_health(self):
        """Подсчет здоровья"""
        self.amount_strength = 0
        for slot, item in self.slots_armor.items():
            if item:
                if hasattr(item, 'value_strength') and item.value_strength:
                    self.amount_strength += item.value_strength
        self.health = self.BASE_HEALTH + self.amount_strength * 10
        self._characteristic.health = self.health

    def calculation_mana(self):
        """Подсчет маны"""
        self.amount_intellect = 0
        for slot, item in self.slots_armor.items():
            if item:
                if hasattr(item, 'value_intellect') and item.value_intellect:
                    self.amount_intellect += item.value_intellect
        self.mana = self.BASE_MANA + self.amount_intellect * 10
        self._characteristic.mana = self.mana

    def calculation_stamina(self):
        """Подсчет выносливости"""
        self.amount_agility = 0
        for slot, item in self.slots_armor.items():
            if item:
                if hasattr(item, 'value_agility') and item.value_agility:
                    self.amount_agility += item.value_agility
        self.stamina = self.BASE_STAMINA + self. amount_agility * 10
        self._characteristic.stamina = self.stamina

    def attack(self):
        """Нанести атаку оружием"""
        if self._weapon:
            print(f"{self._name} атакует {self._weapon.name} с уроном {self._weapon.damage}, категория оружия {self._weapon.category}")
        else:
            print(f'{self._name} атакует голыми руками (урон 1)')

    def info_characteristic(self):
        """Показать характеристики героя"""
        pass
        #print(f"У героя {self._characteristic.health} здоровья, {self._characteristic.mana} маны, {self._characteristic.stamina} выносливости.")


weapon_1 = Weapon('Фростморн', 50, 'Меч')
crown = Helmet('Шлем Господства', 'Шлем', 'Сила', 5, 'Ловкость', 7,  'Интеллект', 3)
chestplate = Chestplate('Шипастый латный нагрудник', 'Нагрудник', 'Сила', 12, 'Ловкость', 15, 'Интеллект', 5)
greaves = Greaves('Шипастые латные поножи', 'Поножи', 'Сила', 10, 'Ловкость', 12, 'Интеллект', 4)
boots = Boots('Латные ботинки короля мертвых', 'Ботинки', 'Сила', 6, 'Ловкость', 11, 'Интеллект', 3)
#
inventory_hero = Inventory()
inventory_hero.add_in_inventory(crown)
inventory_hero.add_in_inventory(chestplate)
inventory_hero.add_in_inventory(greaves)
inventory_hero.add_in_inventory(boots)

hero = Hero('Артас', weapon_1)
hero.attack()

hero.equip_armor(inventory_hero, 'Шлем', 'Шлем Господства')
hero.equip_armor(inventory_hero, 'Нагрудник', 'Шипастый латный нагрудник')
hero.equip_armor(inventory_hero, 'Поножи', 'Шипастые латные поножи')
hero.equip_armor(inventory_hero, 'Ботинки', 'Латные ботинки короля мертвых')

hero.calculation_health()
print(hero.health)
hero.calculation_mana()
print(hero.mana)
hero.calculation_stamina()
print(hero.stamina)
hero.info_characteristic()