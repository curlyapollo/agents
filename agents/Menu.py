import json


class Menu:
    def __init__(self):
        pass

    def get_menu(self) -> json:
        with open("input_files/menu.json", "r") as fin:
            menu_dct = json.load(fin)
        with open("input_files/dish_cards.json", "r") as dishes:
            dishes_dct = json.load(dishes)
        ans = []
        for food in menu_dct["menu_dishes"]:
            card_id = food["menu_dish_card"]
            for dish in dishes_dct["dish_cards"]:
                if dish["card_id"] == card_id:
                    ans.append(dish["dish_name"])
                    break
        return {
            "dishes": ans
        }



menu = Menu()
