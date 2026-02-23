
class Level:
    def __init__(self, lvl=1, exp_gained=0, experience=0, current_exp=0, exp_needed=100):
        self._lvl = lvl
        self.exp_gained = exp_gained
        self.experience = experience
        self.current_exp = current_exp
        self.exp_needed = exp_needed
        self.exp_to_next_level = 0

    def info_lvl(self):
        return 'Показывает уровень героя/врага'


class HeroLevel(Level):
    def __init__(self, hero, lvl=1, experience=0, current_exp=0, exp_gained=0, exp_needed=100):
        super().__init__(lvl, experience, current_exp, exp_gained, exp_needed)
        self.hero = hero

    def info_lvl(self):
        return (f'Уровень:{self._lvl}\n'
                f'Опыт: {self.current_exp}/{self.exp_needed}')

    def up_lvl(self):
        """Добавление опыта, обновление уровня"""
        self.current_exp += self.exp_gained
        # Проверка условия: работает если опыта больше, чем нужно для уровня. Остаток храниться
        while self.current_exp >= self.exp_needed:
            self.current_exp = int(self.current_exp - self.exp_needed)
            self._lvl += 1
            self.exp_needed = int(self.exp_needed * 1.5)


class EnemyLevel(Level):
    def __init__(self, lvl, enemy):
        super().__init__(lvl)
        self.enemy = enemy

    def info_lvl(self):
        return f'Враг:{self.enemy.name}\nУровень:{self._lvl}'
