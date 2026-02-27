
class Enemy:
    def __init__(self, name, health, damage, exp_reward):
        self.name = name
        self.health = health
        self.damage = damage
        self.exp_reward = exp_reward

    def take_damage(self, damage):
        """Получение урона"""
        self.health -= damage
        if self.health <= 0:
            self.health = 0

    def attack(self, target):
        """Нанесение урона"""
        target.take_damage(self.damage)




    def __repr__(self):
        return (f'Имя: {self.name}\nОчки здоровья: {self.health}\nНаносимый урон: {self.damage}\n'
                f'Опыт за убийство: {self.exp_reward}')


