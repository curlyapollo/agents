import json

from Cooker import Cooker
from Menu import menu
class MainAgent:

    Cookers = []

    def __init__(self):
        json_input = json.loads(open('input_files/cookers.json').read())
        try:
            for elem in json_input['cookers']:
                self.Cookers.append(Cooker(elem))
        except:
            print("Incorrect cookers file")

    def make_order(self, data: json) -> json:
        i = 0
        while not self.Cookers[i].is_active():
            i = (i + 1) % len(self.Cookers)
        return self.Cookers[i].make_order(data)

    def get_menu(self) -> json:
        return menu.get_menu()

main_agent = MainAgent()