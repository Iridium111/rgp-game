

class Battle:
    """Бой"""
    def __init__(self):
        self.hero = None
        self.enemy = None

    def start_battle(self, hero, enemy):
        """Старт боя"""
        print(f'Первый ход за {hero._name}')
        print('Начало битвы:\n')

        enemy.generation_of_health(hero.characteristic.stats['health'])
        enemy.generation_level(hero.lvl.lvl)

        while hero.current_health > 0 and enemy.health > 0:

            print(f"{hero._name} vs {enemy.name}\nЗдоровье:\n{hero.current_health}:{hero.characteristic.stats['health']}/{enemy.health}\n"
                  f"Уровни:\n{hero.lvl.lvl}:{enemy.lvl}")

            hero.attack(enemy)
            if enemy.health <= 0:
                print(f'{enemy.name} повержен!\n')
                # Добавление опыта с убийства врага в опыт героя
                exp = enemy.exp_reward
                hero.lvl.add_exp(exp)
                print(f'Получено опыта: {exp}\n')
                break

            enemy.attack(hero)
            if hero.current_health <= 0:
                print('GAME OVER!\n')
                break








