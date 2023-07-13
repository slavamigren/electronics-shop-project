import pytest
from src.phone import Phone


@pytest.fixture
def iphone():
    return Phone('iPhone', 50000, 10, 1)


def test_phone_init(iphone):
    assert iphone.name == 'iPhone'
    assert iphone.price == 50000
    assert iphone.quantity == 10
    assert iphone.number_of_sim == 1
    assert type(iphone.all[-1]) == Phone


def test__repr__(iphone):
    assert repr(iphone) == "Phone('iPhone', 50000, 10, 1)"


def test_sim_setter(iphone):
    with pytest.raises(ValueError):
        iphone.number_of_sim = 0
    iphone.number_of_sim = 2
    assert iphone.number_of_sim == 2
