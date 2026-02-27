

class Battle:
    """Бой"""
    def __init__(self):
        self.hero = ''
        self.enemy = ''

    def start_battle(self, hero, enemy):
        """Старт боя"""
        print(f'Первый ход за {hero._name}')
        print('Начало битвы:\n')

        while hero.characteristic.stats['health'] > 0 and enemy.health > 0:

            print(f"Здоровье:\n{hero.characteristic.stats['health']}:{enemy.health}\n")

            hero.attack(enemy)
            print(f'Герой наносит удар с уроном  {hero.characteristic.damage}')
            if enemy.health <= 0:
                print(f'{enemy.name} повержен!')
                break

            print(f'{enemy.name} наносит удар с уроном {enemy.damage}\n')
            enemy.attack(hero)
            if hero.characteristic.stats['health'] <= 0:
                print('GAME OVER!')
                break








