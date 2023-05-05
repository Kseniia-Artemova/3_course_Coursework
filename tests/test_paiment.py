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
    assert operation_amount.get_currency_name() == "USD"


def test_set_operation_amount_incorrect(pay):
    pay.set_operation_amount({'amount': '56516.3', 'currency': {'name': 'USD', 'code': 'USD'}})
    operation_amount = pay.get_operation_amount()
    assert operation_amount.get_amount() == "Incorrect amount!"
    assert operation_amount.get_currency_name() == "USD"

    pay.set_operation_amount({'amount': '56516.a3', 'currency': {'name': 'руб.', 'code': 'RUB'}})
    operation_amount = pay.get_operation_amount()
    assert operation_amount.get_amount() == "Incorrect amount!"
    assert operation_amount.get_currency_name() == "руб."

    pay.set_operation_amount({'amount': '-56516.03', 'currency': {'name': '', 'code': 'USD'}})
    operation_amount = pay.get_operation_amount()
    assert operation_amount.get_amount() == "Incorrect amount!"
    assert operation_amount.get_currency_name() is None

    pay.set_operation_amount({'amount': '565163', 'currency': {'name': 0, 'code': 'USD'}})
    operation_amount = pay.get_operation_amount()
    assert operation_amount.get_amount() == "Incorrect amount!"
    assert operation_amount.get_currency_name() is None


def test_set_description(pay):
    pay.set_description('Перевод с карты на карту')
    assert pay.get_description() == 'Перевод с карты на карту'


def test_set_description_none(pay):
    pay.set_description("")
    assert pay.get_description() is None


def test_set_description_not_str(pay):
    pay.set_description(True)
    assert pay.get_description() is None


def test_set_pay_from(pay):
    pay.set_pay_from('Счет 33355011456314142963')
    assert pay.get_pay_from() == 'Счет 33355011456314142963'


def test_set_pay_from_empty(pay):
    pay.set_pay_from('')
    assert pay.get_pay_from() == "Incorrect account or card number!"


def test_set_pay_from_incorrect(pay):
    pay.set_pay_from('Maestro 8609654751155')
    assert pay.get_pay_from() == "Incorrect account or card number!"


def test_set_pay_to(pay):
    pay.set_pay_to('Maestro 8602249654751155')
    assert pay.get_pay_to() == 'Maestro 8602249654751155'


def test_set_pay_to_empty(pay):
    pay.set_pay_to('')
    assert pay.get_pay_to() == "Incorrect account or card number!"


def test_set_pay_to_too_short_number(pay):
    pay.set_pay_to('Счет 4573591729755908868')
    assert pay.get_pay_to() == "Incorrect account or card number!"


def test_set_pay_to_incorrect_number(pay):
    pay.set_pay_to('МИР 521127741822846A9')
    assert pay.get_pay_to() == "Incorrect account or card number!"
