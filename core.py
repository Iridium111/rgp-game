

def game_loop(hero, enemy, battle, inventory_hero):
    """Основное меню игры"""
    print('=== НАЧАЛО ИГРЫ ===\n')
    while True:
        print('Выберете начальное действие:')
        print('1.Инвентарь.')
        print('2.Действие.')
        print('3.Бой.')
        print('4.Показать характеристики.')
        print('5.Выход.')

        try:
            action = int(input())
            if action == 1:
                inventory_hero.show_inventory()

            elif action == 2:
                while True:
                    print('1.Надеть предмет.')
                    print('2.Снять предмет.')
                    print('3.Назад.')
                    try:
                        action = int(input())
                        if action == 1:
                            print('Выберете вещь:')
                            for name in inventory_hero.slots_items.keys():
                                print(name)
                            print('\n')
                            item = input()

                            if item in inventory_hero.slots_items:
                                hero.equip_armor(inventory_hero, item)

                            else:
                                print('Нет такого предмета.')

                        elif action == 2:
                            print('Выберете слот:')
                            name = input()
                            if name in hero.slots_equipment:
                                hero.unequip_armor(name, inventory_hero)
                            else:
                                print('Такого слота нет.')
                        elif action == 3:
                            break
                        else:
                            print('Неверное значение!\n')

                    except ValueError:
                        print('Ошибка: нужно ввести число!\n')

            elif action == 3:
                battle.start_battle(hero, enemy)

            elif action == 4:
                hero.info_characteristic()

            elif action == 5:
                break

            else:
                print('Неверное значение!\n')

        except ValueError:
            print('Ошибка: нужно ввести число!\n')
