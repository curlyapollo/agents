import json

from Equipment import Equipment
from EquipmentType import EquipmentType
from Product import Product
from ProductType import ProductType


class Stock:
    products = []
    product_types = []
    equipment = []
    equipment_types = []

    def __init__(self):
        self.import_products()
        self.import_product_types()
        self.import_equipment()
        self.import_equipment_types()

    def import_products(self):
        """
        Импортирование списка доступных продуктов из json
        """
        with open("input_files/products.json", "r") as inp:
            info = json.load(inp)  # См input_files, там видно как выглядит json
            for product_attrs in info['products']:
                product = Product(**product_attrs)
                self.products.append(product)

    def import_product_types(self):
        """
        Импортирование списка доступных типов продуктов из json
        """
        with open("input_files/product_types.json", "r") as inp:
            info = json.load(inp)  # См input_files, там видно как выглядит json
            for product_attrs in info['product_types']:
                product = ProductType(**product_attrs)
                self.product_types.append(product)

    def import_equipment(self):
        """
        Импортирование списка доступного оборудования из json
        """
        with open("input_files/equipment.json", "r") as inp:
            info = json.load(inp)  # См input_files, там видно как выглядит json
            for equip_attrs in info['equipment']:
                equip = Equipment(**equip_attrs)
                self.equipment.append(equip)

    def import_equipment_types(self):
        """
        Импортирование списка доступных типов оборудования из json
        """
        with open("input_files/equipment_type.json", "r") as inp:
            info = json.load(inp)  # См input_files, там видно как выглядит json
            for equip_attrs in info['equipment_type']:
                equip = EquipmentType(**equip_attrs)
                self.equipment_types.append(equip)

    def product_request(self, current_product: (int, int)) -> bool:
        """
        Ответ на запрос конкретного продукта
        :param current_product: запрашиваемый продукт в виде кортежа (тип продукта, нужное количество)
        :return: есть ли нужное количество продукта на складе
        """
        for product in self.products:
            if product.prod_item_type == current_product[0]:
                if int(product.prod_item_quantity) - current_product[1] >= 0:
                    print("Со склада передан {}.".format(product.prod_item_name))
                    product.prod_item_quantity = int(product.prod_item_quantity) - current_product[1]
                    return True
        print("Продукт типа {} отсутствует на складе".format(current_product[0]))
        return False

    def equipment_request(self, current_equipment: int) -> bool:
        """
        Ответ на запрос конкретного оборудования
        :param current_equipment: запрашиваемое оборудование в виде числа (типа оборудования)
        :return: Активно ли данное оборудование на складе
        """
        for equip in self.equipment:
            if int(equip.equip_type) == current_equipment:
                if equip.equip_active:
                    print("Со склада передано {}.".format(equip.equip_name))
                    return True
        print("Оборудование типа {} отсутствует на складе".format(current_equipment))
        return False


