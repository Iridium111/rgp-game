
class Characteristic:
    def __init__(self, hero):    # hero - принимает характеристики от своего объекта
        self._hero = hero
        self.BASE_HEALTH = 100
        self.BASE_MANA = 100
        self.BASE_STAMINA = 100
        self.STAT_MULTIPLIER = 10
        self.attributes = {
            'Сила': 0,
            'Ловкость': 0,
            'Интеллект': 0,
            }
        self.stats = {
            'health': 0,
            'mana': 0,
            'stamina': 0,
            }
        self.damage = 0

    def attributes_all(self):
        """Подсчет всех характеристик"""
        for item in self.attributes:
            self.attributes[item] = 0
            self.damage = 1

        for item in self._hero.slots_equipment.values():
            # Добавление атрибутов
            if item:
                strength = item.stats.get('Сила', 0)
                self.attributes['Сила'] += strength

                intellect = item.stats.get('Интеллект', 0)
                self.attributes['Интеллект'] += intellect

                agility = item.stats.get('Ловкость', 0)
                self.attributes['Ловкость'] += agility

            try:
                if item.damage:
                    self.damage += item.damage - self.damage
            except AttributeError:
                pass

        # Увеличение характеристик в зависимости от количества атрибутов + базового значения + множителя
        self.stats['health'] = self.BASE_HEALTH + self.attributes['Сила'] * self.STAT_MULTIPLIER
        self.stats['mana'] = self.BASE_MANA + self.attributes['Интеллект'] * self.STAT_MULTIPLIER
        self.stats['stamina'] = self.BASE_STAMINA + self.attributes['Ловкость'] * self.STAT_MULTIPLIER
