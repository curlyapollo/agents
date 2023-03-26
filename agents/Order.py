from MainAgent import main_agent


class Order:
    def __init__(self, data):
        self.user_id = data['userId']
        self.dish = data['dishName']
        self.order_id = f'order_{self.user_id}'

    def send_order(self):
        """
        Отправляет инфу по заказу, в упр. агента
        :return: json, с информацией о заказе
        """
        data = {
            'dishName': self.dish,  # "Borsch"
            'orderId': self.order_id  # "order_Semen_25"
        }
        return main_agent.make_order(data)
