

class Battle:
    """Бой"""
    def __init__(self):
        self.hero = ''
        self.enemy = ''

    def start_battle(self, hero, enemy):
        """Старт боя"""
        print(f'Первый ход за {hero._name}')
        print('Начало битвы:\n')

        enemy.generation_of_health(hero.characteristic.stats['health'])

        while hero.characteristic.stats['health'] > 0 and enemy.health > 0:

            print(f"Здоровье:\n{hero.characteristic.stats['health']}:{enemy.health}\n")

            hero.attack(enemy)
            if enemy.health <= 0:
                print(f'{enemy.name} повержен!')
                break

            enemy.attack(hero)
            if hero.characteristic.stats['health'] <= 0:
                print('GAME OVER!')
                break








