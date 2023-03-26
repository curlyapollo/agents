import json

from Dish import Dish


class Cooker:
    def __init__(self, data: json):
        self.name = data['cook_name']
        self.id = data['cook_id']
        self.active = data['cook_active']

    def is_active(self):
        return self.active

    def make_order(self, data: json) -> json:
        self.active = False
        dish = Dish(data["dishName"])
        result = dish.make_dish()
        self.active = True
        return result
