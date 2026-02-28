
from game.item import Item, Armor, Weapon
from game.inventory import Inventory
from game.level import EnemyLevel
from game.hero import Hero
from game.battle import Battle
from game.enemy import Enemy


def main():
    crown = Armor(
        name='Шлем Господства',
        slot='Шлем',
        stats={'Сила': 5, 'Ловкость': 7, 'Интеллект': 3}
        )

    chestplate = Armor(
        name='Шипастый латный нагрудник',
        slot='Нагрудник',
        stats={'Сила': 8, 'Ловкость': 11, 'Интеллект': 5}
        )

    greaves = Armor(
        name='Шипастые латные поножи',
        slot='Поножи',
        stats={'Сила': 7, 'Ловкость': 10, 'Интеллект': 4}
        )

    boots = Armor(
        name='Латные ботинки короля мертвых',
        slot='Ботинки',
        stats={'Сила': 4, 'Ловкость': 6, 'Интеллект': 2}
        )

    weapon = Weapon(
        name='Ледянная скорбь',
        slot='Оружие',
        damage=50,
        stats={'Сила': 10, 'Ловкость': 14, 'Интеллект': 4}
        )

    hero = Hero('Артас')
    enemy = Enemy('Скелет', 50, 100)
    battle = Battle()




    inventory_hero = Inventory()
    inventory_hero.add_in_inventory(crown)
    inventory_hero.add_in_inventory(chestplate)
    inventory_hero.add_in_inventory(greaves)
    inventory_hero.add_in_inventory(boots)
    inventory_hero.add_in_inventory(weapon)

    hero.equip_armor(inventory_hero, 'Шлем Господства')
    hero.equip_armor(inventory_hero, 'Шипастый латный нагрудник')
    hero.equip_armor(inventory_hero, 'Шипастые латные поножи')
    hero.equip_armor(inventory_hero, 'Латные ботинки короля мертвых')
    hero.equip_armor(inventory_hero, 'Ледянная скорбь')

    lvlenemy = EnemyLevel(10, enemy)
    print(lvlenemy.info_lvl())

    hero.lvl.exp_gained = 1500
    hero.lvl.up_lvl()

    hero.characteristic.attributes_all()

    hero.info_characteristic()

    battle.start_battle(hero, enemy)


if __name__ == "__main__":
    main()
