
class Characteristic:
    def __init__(self, hero):    # hero - принимает характеристики от своего объекта
        self._hero = hero
        self.BASE_HEALTH = 100
        self.BASE_MANA = 100
        self.BASE_STAMINA = 100
        self.STAT_MULTIPLIER = 10
        self.attributes = {
            'strength': 0,
            'agility': 0,
            'intellect': 0,
            }
        self.stats = {
            'health': 0,
            'mana': 0,
            'stamina': 0,
            }

    def attributes_all(self):
        """Подсчет всех характеристик"""
        for item in self.attributes:
            self.attributes[item] = 0

        for item in self._hero.slots_equipment.values():
            # Добавление атрибутов
            if item:
                if hasattr(item, 'value_strength') and item.value_strength:
                    self.attributes['strength'] += item.value_strength

                if hasattr(item, 'value_intellect') and item.value_intellect:
                    self.attributes['intellect'] += item.value_intellect

                if hasattr(item, 'value_agility') and item.value_agility:
                    self.attributes['agility'] += item.value_agility

        # Увеличение характеристик в зависимости от количества атрибутов + базового значения + множителя
        self.stats['health'] = self.BASE_HEALTH + self.attributes['strength'] * self.STAT_MULTIPLIER
        self.stats['mana'] = self.BASE_MANA + self.attributes['intellect'] * self.STAT_MULTIPLIER
        self.stats['stamina'] = self.BASE_STAMINA + self.attributes['agility'] * self.STAT_MULTIPLIER
