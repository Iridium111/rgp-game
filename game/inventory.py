
class Inventory:
    def __init__(self):
        self.slots_category = {}
        self.slots_items = {}

    def add_in_inventory(self, item):
        """Добавление предметов в инвентарь"""
        # Сохраняем по имени
        self.slots_items[item.name] = item

        # Сохраняем по категориям
        if item.category not in self.slots_category:
            self.slots_category[item.category] = {}     # создаем словарь для этой категории
        self.slots_category[item.category][item.name] = item    # кладем предмет в свою категорию
