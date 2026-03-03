
from random import randint

class Enemy:
    def __init__(self, name, damage, exp_reward):
        self.name = name
        self.health = 0
        self.damage = damage
        self.exp_reward = exp_reward
        self.lvl = 1

    def generation_of_health(self, value):
        """Генерация здоровья противника в зависимости от здоровья героя +-25%"""
        # Минимальное здоровье
        min_health = int(value * 0.75)
        # Максимальное здоровье
        max_health = int(value * 1.25)

        self.health = randint(min_health, max_health)

    def take_damage(self, damage):
        """Получение урона"""
        self.health -= damage
        if self.health <= 0:
            self.health = 0

    def attack(self, target):
        """Нанесение урона"""
        # Минимальное здоровье
        min_damage = int(self.damage * 0.75)
        # Максимальное здоровье
        max_damage = int(self.damage * 1.25)

        damage = randint(min_damage, max_damage)
        target.take_damage(damage)
        print(f'{self.name} наносит удар с уроном  {damage}')

    def generation_level(self, lvl):
        """Генерация уровня противника в завимимости от уровня героя"""
        if lvl == 1:
            min_lvl = 1
            max_lvl = 2
            self.lvl = randint(min_lvl, max_lvl)

        else:
            # +-1 уровень от уровня героя.
            min_lvl = lvl - 1
            max_lvl = lvl + 1
            self.lvl = randint(min_lvl, max_lvl)

    def __repr__(self):
        return (f'Имя: {self.name}\nОчки здоровья: {self.health}\nНаносимый урон: {self.damage}\n'
                f'Опыт за убийство: {self.exp_reward}')


