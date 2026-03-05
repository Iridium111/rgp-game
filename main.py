
from game.item import Item, Armor, Weapon
from game.inventory import Inventory
from game.level import EnemyLevel
from game.hero import Hero
from game.battle import Battle
from game.enemy import Enemy
from core import game_loop


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
    enemy = Enemy('Скелет', 30, 50)
    battle = Battle()

    inventory_hero = Inventory()
    inventory_hero.add_in_inventory(crown)
    inventory_hero.add_in_inventory(chestplate)
    inventory_hero.add_in_inventory(greaves)
    inventory_hero.add_in_inventory(boots)
    inventory_hero.add_in_inventory(weapon)

    game_loop(hero, enemy, battle, inventory_hero)


if __name__ == "__main__":
    main()
