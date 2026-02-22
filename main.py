

class Characteristic:
    def __init__(self, hero):    #hero - принимает характеристики от своего объекта
        self._hero = hero
        self.BASE_HEALTH = 100
        self.BASE_MANA = 100
        self.BASE_STAMINA = 100
        self.STAT_MULTIPLIER = 10
        self.attributes = {
            'strength': 0,
            'agility': 0,
            'intellect': 0,
            }
        self.stats = {
            'health': 0,
            'mana': 0,
            'stamina': 0,
            }

    def attributes_all(self):
        """Подсчет всех характеристик"""
        for item in self.attributes:
            self.attributes[item] = 0

        for item in self._hero.slots_equipment.values():
            if item:
                if hasattr(item, 'value_strength') and item.value_strength:
                    self.attributes['strength'] += item.value_strength

                if hasattr(item, 'value_intellect') and item.value_intellect:
                    self.attributes['intellect'] += item.value_intellect

                if hasattr(item, 'value_agility') and item.value_agility:
                    self.attributes['agility'] += item.value_agility

        self.stats['health'] = self.BASE_HEALTH + self.attributes['strength'] * self.STAT_MULTIPLIER
        self.stats['mana'] = self.BASE_MANA + self.attributes['intellect'] * self.STAT_MULTIPLIER
        self.stats['stamina'] = self.BASE_STAMINA + self.attributes['agility'] * self.STAT_MULTIPLIER


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


class Enemy:
    def __init__(self, name):
        self.name = name

    def attack(self):
        pass

    def __str__(self):
        return f'Информация о {self.name}'


class Skeleton(Enemy):
    def __init__(self, name, health, damage):
        super().__init__(name)
        self.health = health
        self.damage = damage

    # def info_enemy(self):
    #     """Вывод информации о враге."""
    #     return f'{self.name}\nЗдоровье:{self.health}\nУрон:{self.damage}'

    def __str__(self):
        return f'{self.name}\nЗдоровье:{self.health}\nУрон:{self.damage}'


class Level:
    def __init__(self, lvl=1, exp_gained=0, experience=0, current_exp=0, exp_needed=100):
        self._lvl = lvl
        self.exp_gained = exp_gained
        self.experience = experience
        self.current_exp = current_exp
        self.exp_needed = exp_needed
        self.exp_to_next_level = 0

    def info_lvl(self):
        return 'Показывает уровень героя/врага'


class HeroLevel(Level):
    def __init__(self, hero, lvl=1, experience=0, current_exp=0, exp_gained=0, exp_needed=100):
        super().__init__(lvl, experience, current_exp, exp_gained, exp_needed)
        self.hero = hero

    def info_lvl(self):
        return (f'Уровень:{self._lvl}\n'
                f'Опыт: {self.current_exp}/{self.exp_needed}')

    def up_lvl(self):
        """Добавление опыта, обновление уровня"""
        self.current_exp += self.exp_gained
        # Проверка условия: работает если опыта больше, чем нужно для уровня. Остаток храниться
        while self.current_exp >= self.exp_needed:
            self.current_exp = int(self.current_exp - self.exp_needed)
            self._lvl += 1
            self.exp_needed = int(self.exp_needed * 1.5)


class EnemyLevel(Level):
    def __init__(self, lvl, enemy):
        super().__init__(lvl)
        self.enemy = enemy

    def info_lvl(self):
        return f'Враг:{self.enemy.name}\nУровень:{self._lvl}'


class Hero:
    def __init__(self, name):
        self._name = name
        self.characteristic = Characteristic(self)
        self.slots_equipment = {
            'Оружие': None,
            'Шлем': None,
            'Нагрудник': None,
            'Поножи': None,
            'Ботинки': None,
        }
        self.lvl = HeroLevel(self)

    def equip_armor(self, inventory, key, name_thing):
        """Надеть броню"""
        try:
            if key not in self.slots_equipment:
                print('Нет такого слота.')
            if self.slots_equipment[key]:
                print('Слот занят.')

            # Пытаемся получить предмет
            item = inventory.slots_category[key][name_thing]
            self.slots_equipment[key] = item

            # Удаляем из инвентаря
            inventory.slots_category[key].pop(name_thing)
            if not inventory.slots_category[key]:
                inventory.slots_category.pop(key)
            inventory.slots_items.pop(name_thing)

            # Пересчитываем характеристики текущего героя (self)
            self.characteristic.attributes_all()

        except KeyError:
            print(f'Предмет {name_thing} или категория {key} не найдены в инвентаре')

    def unequip_armor(self, name, inventory):
        """Снять броню"""
        item = self.slots_equipment[name]

        # Проверка наличия предмета в слоту и снятие.
        if item:
            inventory.add_in_inventory(item)
            self.slots_equipment[name] = None

            # Пересчитываем характеристики текущего героя (self)
            self.characteristic.attributes_all()
            print(f'Снят: {item}')

        elif not item:
            print('Нет вещи в этом слоту')

    def attack(self):
        """Нанести атаку оружием"""
        pass

    def info_characteristic(self):
        """Показать характеристики героя"""
        print(f"Во что одет наш герой:\n")
        for key, item in self.slots_equipment.items():
            print(item)

        print(f'Информация об уровне:\n{self.lvl.info_lvl()}\n')

        print(f"Показатели здоровья, маны, выносливости:\nЗдоровье: {self.characteristic.stats['health']} \n"
              f"Мана: {self.characteristic.stats['mana']} \nВыносливость: {self.characteristic.stats['stamina']}\n")


crown = Helmet('Шлем Господства', 'Шлем', 'Сила', 5, 'Ловкость', 7,  'Интеллект', 3)
chestplate = Chestplate('Шипастый латный нагрудник', 'Нагрудник', 'Сила', 12, 'Ловкость', 15, 'Интеллект', 5)
greaves = Greaves('Шипастые латные поножи', 'Поножи', 'Сила', 10, 'Ловкость', 12, 'Интеллект', 4)
boots = Boots('Латные ботинки короля мертвых', 'Ботинки', 'Сила', 6, 'Ловкость', 11, 'Интеллект', 3)
weapon = Weapon('Ледянная скорбь', 50, 'Оружие', 'Сила', 10, 'Ловкость', 7)


inventory_hero = Inventory()
inventory_hero.add_in_inventory(crown)
inventory_hero.add_in_inventory(chestplate)
inventory_hero.add_in_inventory(greaves)
inventory_hero.add_in_inventory(boots)
inventory_hero.add_in_inventory(weapon)

enemy = Skeleton('Скелет', 100, 20)
hero = Hero('Артас')
hero.attack()


hero.equip_armor(inventory_hero, 'Шлем', 'Шлем Господства')
hero.equip_armor(inventory_hero, 'Нагрудник', 'Шипастый латный нагрудник')
hero.equip_armor(inventory_hero, 'Поножи', 'Шипастые латные поножи')
hero.equip_armor(inventory_hero, 'Ботинки', 'Латные ботинки короля мертвых')
hero.equip_armor(inventory_hero, 'Оружие', 'Ледянная скорбь')

print(inventory_hero.slots_category)


lvlenemy = EnemyLevel(10, enemy)
print(lvlenemy.info_lvl())

hero.lvl.exp_gained = 1500
hero.lvl.up_lvl()

hero.characteristic.attributes_all()

hero.info_characteristic()
