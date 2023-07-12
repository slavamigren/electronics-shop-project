import pytest
from src.item import Item


@pytest.fixture
def keyboard():
    return Item('keyboard', 5000, 10)


def test_item_init(keyboard):
    assert keyboard.name == 'keyboard'
    assert keyboard.price == 5000
    assert keyboard.quantity == 10
    assert type(keyboard.all[-1]) == Item


def test_item_calculate_total_price(keyboard):
    assert keyboard.calculate_total_price() == 50000


def test_item_apply_discoun(keyboard):
    keyboard.pay_rate = 0.8
    keyboard.apply_discount()
    assert keyboard.price == 4000


def test_name_setter(keyboard):
    assert keyboard.name == 'keyboard'
    keyboard.name = 'keyboardSuperPuper'
    assert keyboard.name == 'keyboardSu'


def test_instantiate_from_csv(keyboard):
    Item.instantiate_from_csv()
    assert len(Item.all) == 6


def test_string_to_number(keyboard):
    assert keyboard.string_to_number('5') == 5
    assert keyboard.string_to_number('5.0') == 5
    assert keyboard.string_to_number('5.5') == 5