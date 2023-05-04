import pytest
import scr.payment as pay_


@pytest.fixture
def pay():
    return pay_.Payment()


def test_set_date_correct(pay):
    pay.set_date('2019-08-26T10:50:58.294041')
    assert pay.get_date() == "26.08.2019"


def test_set_date_incorrect(pay):
    pay.set_date('2019-08-26C10:50:58.294041')
    assert pay.get_date() == "Invalid date format!"
    pay.set_date('2019-08-2T10:50:58.294041')
    assert pay.get_date() == "Invalid date format!"
    pay.set_date('201A-08-20T10:50:58.294041')
    assert pay.get_date() == "Invalid date format!"
    pay.set_date('20190-08-20T10:50:58.294041')
    assert pay.get_date() == "Invalid date format!"
    pay.set_date('2019008-20T10:50:58.294041')
    assert pay.get_date() == "Invalid date format!"
    pay.set_date('')
    assert pay.get_date() == "Invalid date format!"
    pay.set_date('2019-04-31T10:50:58.294041')
    assert pay.get_date() == "Invalid date format!"


def test_set_operation_amount_correct(pay):
    pay.set_operation_amount({'amount': '56516.63', 'currency': {'name': 'USD', 'code': 'USD'}})
    operation_amount = pay.get_operation_amount()
    assert operation_amount.get_amount() == "56516.63"


def test_set_operation_amount_incorrect(pay):
    pay.set_operation_amount({'amount': '56516.3', 'currency': {'name': 'USD', 'code': 'USD'}})
    operation_amount = pay.get_operation_amount()
    assert operation_amount.get_amount() == "Incorrect amount!"

    pay.set_operation_amount({'amount': '56516.a3', 'currency': {'name': 'USD', 'code': 'USD'}})
    operation_amount = pay.get_operation_amount()
    assert operation_amount.get_amount() == "Incorrect amount!"

    pay.set_operation_amount({'amount': '-56516.03', 'currency': {'name': 'USD', 'code': 'USD'}})
    operation_amount = pay.get_operation_amount()
    assert operation_amount.get_amount() == "Incorrect amount!"

    pay.set_operation_amount({'amount': '565163', 'currency': {'name': 'USD', 'code': 'USD'}})
    operation_amount = pay.get_operation_amount()
    assert operation_amount.get_amount() == "Incorrect amount!"




