
from game.item import Helmet, Chestplate, Greaves, Boots, Weapon
from game.inventory import Inventory
from game.enemy import Skeleton
from game.level import EnemyLevel
from game.hero import Hero


def main():
    crown = Helmet('Шлем Господства', 'Шлем', 'Сила', 5, 'Ловкость',
                             7,  'Интеллект', 3)

    chestplate = Chestplate('Шипастый латный нагрудник', 'Нагрудник', 'Сила',
                                      12, 'Ловкость', 15, 'Интеллект', 5)

    greaves = Greaves('Шипастые латные поножи', 'Поножи', 'Сила', 10,
                                'Ловкость', 12, 'Интеллект', 4)

    boots = Boots('Латные ботинки короля мертвых', 'Ботинки', 'Сила', 6,
                            'Ловкость', 11, 'Интеллект', 3)

    weapon = Weapon('Ледянная скорбь', 50, 'Оружие', 'Сила', 10,
                              'Ловкость', 7)


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

    hero.unequip_armor('Нагрудник', inventory_hero)

    hero.characteristic.attributes_all()

    hero.info_characteristic()


if __name__ == "__main__":
    main()
