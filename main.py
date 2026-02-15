
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
        self.health = 0


class Armor:
    def __init__(self, name, characteristic, value, slot):
        self.name = name
        self.characteristic = characteristic
        self.value = value
        self.slot = slot


class Helmet(Armor):
    def __init__(self, name, characteristic, value):
        super().__init__(name, characteristic, value, slot="helmet")

    def __repr__(self):
        return f'{self.name}, {self.characteristic} {self.value}\n'


class Chestplate(Armor):
    def __init__(self, name, characteristic, value):
        super().__init__(name, characteristic, value, slot="chestplate")

    def __repr__(self):
        return f'{self.name}, {self.characteristic} {self.value}\n'


class Greaves(Armor):
    def __init__(self, name, characteristic, value):
        super().__init__(name, characteristic, value, slot="greaves")

    def __repr__(self):
        return f'{self.name}, {self.characteristic} {self.value}\n'


class Boots(Armor):
    def __init__(self, name, characteristic, value):
        super().__init__(name, characteristic, value, slot="boots")

    def __repr__(self):
        return f'{self.name}, {self.characteristic} {self.value}\n'


class Hero:
    def __init__(self, name, weapon):
        self._name = name
        self._characteristic = Characteristic(100, 100, self,)   #self - для передачи характеристик в Characteristic
        self._weapon = weapon
        self.BASE_HEALTH = 100
        self.slots_armor = {
            'helmet': None,
            'chestplate': None,
            'greaves': None,
            'boots': None,
        }
        self.amount_strength = 0
        self.health = 0

    def equip_armor(self, item):
        """Одевание брони"""
        self.slots_armor[item.slot] = item
        self.amount_strength += item.value

    def calculation_health(self):
        """Подсчет здоровья"""
        self.health = self.BASE_HEALTH + self.amount_strength * 10
        self._characteristic.health = self.health

    def attack(self):
        """Нанести атаку оружием"""
        if self._weapon:
            print(f"{self._name} атакует {self._weapon.name} с уроном {self._weapon.damage}, категория оружия {self._weapon.category}")
        else:
            print(f'{self._name} атакует голыми руками (урон 1)')

    def info_characteristic(self):
        """Показать характеристики героя"""
        print(f"У героя {self._characteristic.health} здоровья, {self._characteristic.mana} маны, {self._characteristic.stamina} выносливости.")


weapon_1 = Weapon('Фростморн', 50, 'Меч')

hero = Hero('Артас', weapon_1)
hero.attack()

crown = Helmet('Шлем Господства', 'сила', 5)
chestplate = Chestplate('Шипастый латный нагрудник', 'сила', 10)
greaves = Greaves('Шипастые латные поножи', 'сила', 4)
boots = Boots('Латные ботинки короля мертвых', 'сила', 3)

hero.equip_armor(crown)
hero.equip_armor(chestplate)
hero.equip_armor(greaves)
hero.equip_armor(boots)
hero.calculation_health()

print(hero.slots_armor)
hero.info_characteristic()