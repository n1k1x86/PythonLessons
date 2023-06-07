from tasks.hw2 import Order, MorningDiscount, ElderDiscount


def test_morning_disc_positive():
    test_order = Order(100, MorningDiscount())
    assert test_order.final_price() == 75


def test_morning_disc_negative():
    test_order = Order(100, MorningDiscount())
    assert test_order.final_price() != 10


def test_elder_disc_positive():
    test_order = Order(100, ElderDiscount())
    assert test_order.final_price() == 10


def test_elder_disc_negative():
    test_order = Order(100, ElderDiscount())
    assert test_order.final_price() != 75
