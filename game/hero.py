
from .characters import Characteristic
from .level import HeroLevel
from .inventory import Inventory
from random import randint


class Hero:
    """Главный герой игры."""

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

    def equip_armor(self, inventory, name_thing):
        """Надеть броню"""
        # Получаем предмет из инвентаря
        item = inventory.slots_items.get(name_thing)
        if not item:
            print(f'Предмет {name_thing} не найден.')
            return

        # Проверяем слот
        if item.slot not in self.slots_equipment:
            print(f'Нет такого слота {item.slot}')
            return

        # Проверяем, свободен ли слот
        if self.slots_equipment[item.slot]:
            print(f'Слот {item.slot} занят.')
            return

        # Надеваем
        self.slots_equipment[item.slot] = item

        # Удаление из инвентаря
        inventory.slots_category[item.slot].pop(name_thing)
        if not inventory.slots_category[item.slot]:
            inventory.slots_category.pop(item.slot)
        inventory.slots_items.pop(name_thing)

        # Обновление характеристик
        self.characteristic.attributes_all()

    def unequip_armor(self, slot_name, inventory):
        """Снять броню"""
        thing = self.slots_equipment[slot_name]

        # Проверка наличия предмета в слоту и снятие.
        if thing:
            inventory.add_in_inventory(thing)
            self.slots_equipment[slot_name] = None

            # Пересчитываем характеристики текущего героя (self)
            self.characteristic.attributes_all()
            print(f'Снят: {thing}')

        elif not thing:
            print('Нет вещи в этом слоту')

    def take_damage(self, damage):
        """Получение урона"""
        self.characteristic.stats['health'] -= damage
        if self.characteristic.stats['health'] <= 0:
            self.characteristic.stats['health'] = 0

    def attack(self, target):
        """Нанести атаку оружием"""
        # Минимальное здоровье
        min_damage = int(self.characteristic.damage * 0.75)
        # Максимальное здоровье
        max_damage = int(self.characteristic.damage * 1.25)

        damage = randint(min_damage, max_damage)
        target.take_damage(damage)
        print(f'{self._name} наносит удар с уроном  {damage}')

    def info_characteristic(self):
        """Показать характеристики героя"""
        print(f"Во что одет наш герой:\n")
        for key, thing in self.slots_equipment.items():
            print(thing)

        print(f'Информация об уровне:\n{self.lvl.info_lvl()}\n')

        print(f"Показатели здоровья, маны, выносливости:\nЗдоровье: {self.characteristic.stats['health']} \n"
              f"Мана: {self.characteristic.stats['mana']} \nВыносливость: {self.characteristic.stats['stamina']}\n")
