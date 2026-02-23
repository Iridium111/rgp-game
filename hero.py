
from characters import Characteristic
import level

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
        self.lvl = level.HeroLevel(self)

    def equip_armor(self, inventory, key, name_thing):
        """Надеть броню"""
        try:
            if key not in self.slots_equipment:
                print('Нет такого слота.')
                return

            if self.slots_equipment[key]:
                print('Слот занят.')
                return

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
            return

    def unequip_armor(self, name, inventory):
        """Снять броню"""
        thing = self.slots_equipment[name]

        # Проверка наличия предмета в слоту и снятие.
        if thing:
            inventory.add_in_inventory(thing)
            self.slots_equipment[name] = None

            # Пересчитываем характеристики текущего героя (self)
            self.characteristic.attributes_all()
            print(f'Снят: {thing}')

        elif not thing:
            print('Нет вещи в этом слоту')

    def attack(self):
        """Нанести атаку оружием"""
        pass

    def info_characteristic(self):
        """Показать характеристики героя"""
        print(f"Во что одет наш герой:\n")
        for key, thing in self.slots_equipment.items():
            print(thing)

        print(f'Информация об уровне:\n{self.lvl.info_lvl()}\n')

        print(f"Показатели здоровья, маны, выносливости:\nЗдоровье: {self.characteristic.stats['health']} \n"
              f"Мана: {self.characteristic.stats['mana']} \nВыносливость: {self.characteristic.stats['stamina']}\n")
