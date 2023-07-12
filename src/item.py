import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value[:10] # если строка длиннее 10 символов, обрезает


    @staticmethod
    def string_to_number(string):
        return int(float(string))


    @classmethod
    def instantiate_from_csv(cls):
        with open('../src/items.csv') as file:
            items = csv.DictReader(file)
            for item in items:
                Item(item['name'], float(item['price']), int(item['quantity']))


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
