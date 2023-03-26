import json
from Stock import Stock


class Dish:
    def __init__(self, name: str):
        self.name = name

    def make_dish(self) -> json:
        time = -1
        dish_id = -1
        stock = Stock()
        stock.import_products()
        stock.import_equipment()
        stock.import_product_types()
        stock.import_equipment_types()
        with open("input_files/dish_cards.json", "r") as inp:
            info = json.load(inp)
            for dish_attrs in info["dish_cards"]:
                if dish_attrs["dish_name"] == self.name:
                    time = dish_attrs["card_time"]
                    dish_id = dish_attrs["card_id"]
                    for oper in dish_attrs["operations"]:
                        time += oper["oper_time"]
                        equip_type = dish_attrs["equip_type"]
                        if not stock.equipment_request(equip_type):
                            return {
                                "time": 0,
                                "dishName": self.name,
                                "dishId": -1
                            }
                        for prod in oper["oper_products"]:
                            prod_type = prod["prod_type"]
                            prod_quantity = prod["prod_quantity"]
                            if not stock.product_request((prod_type, prod_quantity)):
                                return {
                                    "time": 0,
                                    "dishName": self.name,
                                    "dishId": -1
                                }
                    break
        if time == -1:
            print("no dish " + self.name + " in cards")
            return {
                "time": 0,
                "dishName": self.name,
                "dishId": -1
            }
        return {
            "time": time,
            "dishName": self.name,
            "dishId": dish_id
        }
