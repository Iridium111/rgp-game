
class Level:
    def __init__(self, lvl=1, current_exp=0, exp_needed=100):
        self.lvl = lvl
        self.current_exp = current_exp
        self.exp_needed = exp_needed


    def info_lvl(self):
        return 'Показывает уровень героя/врага'

class HeroLevel(Level):
    def __init__(self, hero, lvl=1, current_exp=0, exp_needed=100):
        super().__init__(lvl, current_exp, exp_needed)
        self.hero = hero

    def info_lvl(self):
        return (f'Уровень:{self.lvl}\n'
                f'Опыт: {self.current_exp}/{self.exp_needed}')

    def add_exp(self, exp):
        self.current_exp += exp
        # Проверка условия: работает если опыта больше, чем нужно для уровня. Остаток храниться
        while self.current_exp >= self.exp_needed:
            self.current_exp = int(self.current_exp - self.exp_needed)
            self.lvl += 1
            self.exp_needed = int(self.exp_needed * 1.5)


class EnemyLevel(Level):
    def __init__(self, lvl, enemy):
        super().__init__(lvl)
        self.enemy = enemy

    def info_lvl(self):
        return f'Враг:{self.enemy.name}\nУровень:{self.lvl}'
