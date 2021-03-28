import pytest

from src.checkout.Checkout import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.add_item_with_price("a", 1)
    checkout.add_item_with_price("b", 2)
    return checkout


def test_can_add_item_price(checkout):
    checkout.add_item_with_price("aaaaaa", 1)


def test_can_add_item_to_cart(checkout):
    checkout.add_item_to_cart("a")


def test_can_calculate_current_total_single_item(checkout):
    checkout.add_item_to_cart("a")
    assert checkout.calculate_total() == 1


def test_can_calculate_current_total_multiple_items(checkout):
    checkout.add_item_to_cart("a")
    checkout.add_item_to_cart("b")
    assert checkout.calculate_total() == 3


def test_can_add_discount_rule(checkout):
    checkout.add_discount("a", 3, 2)


def test_can_apply_discount_rule(checkout):
    checkout.add_discount("a", 3, 2)
    checkout.add_item_to_cart("a")
    checkout.add_item_to_cart("a")
    checkout.add_item_to_cart("a")
    assert checkout.calculate_total() == 2

def test_exception_is_raised_when_adding_unknown_item_to_cart(checkout):
    with pytest.raises(Exception):
        checkout.add_item_to_cart("c")