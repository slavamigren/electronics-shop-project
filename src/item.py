import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """Создание экземпляра класса item."""
        super().__init__()
        self._name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value[:10]  # если строка длиннее 10 символов, обрезает

    @staticmethod
    def string_to_number(string):
        """Переводит str в int, обрезая дробную часть"""
        return int(float(string))

    @classmethod
    def instantiate_from_csv(cls):
        """Загружает из файла список товаров"""
        with open('../src/items.csv') as file:
            items = csv.DictReader(file)
            for item in items:
                Item(item['name'], float(item['price']), int(item['quantity']))

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        return NotImplemented

    def calculate_total_price(self) -> float:
        """Рассчитывает общую стоимость конкретного товара в магазине."""
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
