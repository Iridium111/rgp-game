
class Enemy:
    def __init__(self, name):
        self.name = name

    def attack(self):
        pass

    def __str__(self):
        return f'Информация о {self.name}'


class Skeleton(Enemy):
    def __init__(self, name, health, damage):
        super().__init__(name)
        self.health = health
        self.damage = damage

    def __str__(self):
        return f'{self.name}\nЗдоровье:{self.health}\nУрон:{self.damage}'
