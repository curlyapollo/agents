import random
from Order import Order
from MainAgent import main_agent


class Customer:
    def __init__(self, name, wish_dish):
        self.name = name if name else 'Semen'
        self.id = f'{self.name}_{random.randint(0, 100)}'
        self.wish_dish = wish_dish if wish_dish else 'Borsch'

    def _make_order(self, dish_name):
        """
        :param dish_name: Имя блюда (str)
        :return: json, с информацией о заказе
        """
        data = {
            'userId': self.id,
            'dishName': dish_name
        }
        order = Order(data)
        return order.send_order()

    def _get_menu(self):
        """
        Получить Меню
        :return: Меню
        """
        return main_agent.get_menu()

    def _choose_dish(self, menu):
        """
        Выбор блюда
        :param menu: json с меню
        :return: str, имя блюда
        """
        if self.wish_dish in menu['dishes']:
            return self.wish_dish
        else:
            return random.choice(menu['dishes'])

    def restaurant_event(self):
        """
        Поход в ресторан (основной метод посетителя)
        :return: json, с информацией о заказе
        """
        menu = self._get_menu()
        choice = self._choose_dish(menu)
        return self._make_order(choice)

    def get_id(self):
        """
        Получить id пользователя вида: <имя>_<число>
        :return: Id
        """
        return self.id