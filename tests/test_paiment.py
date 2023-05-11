import pytest
from classes.payment import Payment
from datetime import datetime


@pytest.fixture
def pay():
    return Payment()


def test___str__(pay):
    pay.id_pay = 542678139
    assert str(pay) == f"Payment 542678139, more detailed information is closed."


def test___repr__(pay):
    assert repr(pay) == ('Payment('
                         '_Payment__id_pay=None, '
                         '_Payment__state_pay=None, '
                         '_Payment__date_pay=None, '
                         '_Payment__operation_amount_pay=None, '
                         '_Payment__description_pay=None, '
                         '_Payment__from_pay=None, '
                         '_Payment__to_pay=None)')


def test_id_pay_correct(pay):
    pay.id_pay = 441945886
    assert pay.id_pay == 441945886


def test_id_pay_incorrect(pay):
    pay.id_pay = "441945886"
    assert pay.id_pay is None

    pay.id_pay = True
    assert pay.id_pay is None

    pay.id_pay = 4419458.86
    assert pay.id_pay is None


def test_state_pay_executed(pay):
    pay.state_pay = "EXECUTED"
    assert pay.state_pay == "EXECUTED"

    pay.state_pay = "executed"
    assert pay.state_pay == "EXECUTED"


def test_state_pay_canceled(pay):
    pay.state_pay = "CANCELED"
    assert pay.state_pay == "CANCELED"

    pay.state_pay = "canceled"
    assert pay.state_pay == "CANCELED"


def test_state_pay_incorrect(pay):
    pay.state_pay = "CANCEL"
    assert pay.state_pay is None

    pay.state_pay = "успешная"
    assert pay.state_pay is None

    pay.state_pay = 1
    assert pay.state_pay is None

    pay.state_pay = True
    assert pay.state_pay is None


def test_date_pay_correct(pay):
    pay.date_pay = "2018-10-14T08:21:33.419441"
    assert pay.date_pay == datetime(2018, 10, 14, 8, 21, 33, 419441)


def test_date_pay_incorrect(pay):
    pay.date_pay = "2018-13-14T08:21:33.419441"
    assert pay.date_pay is None

    pay.date_pay = "2018-10-14T28:21:33.419441"
    assert pay.date_pay is None

    pay.date_pay = "2018-11-31T08:21:33.419441"
    assert pay.date_pay is None

    pay.date_pay = 20181131
    assert pay.date_pay is None

    pay.date_pay = "2012-02-30T08:21:33.419441"
    assert pay.date_pay is None

    pay.date_pay = "2013-02-29T08:21:33.419441"
    assert pay.date_pay is None

    pay.date_pay = "2013-02-29"
    assert pay.date_pay is None

    pay.date_pay = True
    assert pay.date_pay is None


def test_operation_amount_pay_correct(pay):
    pay.operation_amount_pay = {
        "amount": "77751.04",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    }
    assert pay.operation_amount_pay == ("77751.04", "руб.")

    pay.operation_amount_pay = {
        "amount": "77751",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    }
    assert pay.operation_amount_pay == ("77751.00", "руб.")

    pay.operation_amount_pay = {
        "amount": 77751,
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    }
    assert pay.operation_amount_pay == ("77751.00", "руб.")


def test_operation_amount_pay_incorrect(pay):
    pay.operation_amount_pay = {}
    assert pay.operation_amount_pay is None

    pay.operation_amount_pay = None
    assert pay.operation_amount_pay is None

    pay.operation_amount_pay = {
        "amount": "77751.04",
        "currency": {
            "name": 1,
            "code": "RUB"
        }
    }
    assert pay.operation_amount_pay is None

    pay.operation_amount_pay = {
        "amount": "77751.04",
        "currency": {
            "name": "",
            "code": "RUB"
        }
    }
    assert pay.operation_amount_pay is None

    pay.operation_amount_pay = {
        "amount": "77751.04",
        "currency": {}
    }
    assert pay.operation_amount_pay is None

    pay.operation_amount_pay = {
        "amount": True,
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    }
    assert pay.operation_amount_pay is None

    pay.operation_amount_pay = {
        "amount": False,
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    }
    assert pay.operation_amount_pay is None

    pay.operation_amount_pay = {
        "amount": "тридцать",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    }
    assert pay.operation_amount_pay is None


def test_description_pay_correct(pay):
    pay.description_pay = "Перевод с карты на счет"
    assert pay.description_pay == "Перевод с карты на счет"


def test_description_pay_incorrect(pay):
    pay.description_pay = True
    assert pay.description_pay is None

    pay.description_pay = 4
    assert pay.description_pay is None


def test_from_pay_correct(pay):
    pay.from_pay = "Maestro 4598300720424501"
    assert pay.from_pay == ("Maestro", "4598300720424501")

    pay.from_pay = "Visa Gold 9447344650495960"
    assert pay.from_pay == ("Visa Gold", "9447344650495960")

    pay.from_pay = "Счет 97584898735659638967"
    assert pay.from_pay == ("Счет", "97584898735659638967")


def test_from_pay_incorrect(pay):
    pay.from_pay = "Maestro4598300720424501"
    assert pay.from_pay is None

    pay.from_pay = "Maestro-4598300720424501"
    assert pay.from_pay is None

    pay.from_pay = "Visa-Gold-944734465095960"
    assert pay.from_pay is None

    pay.from_pay = 4598300720424501
    assert pay.from_pay is None

    pay.from_pay = True
    assert pay.from_pay is None

    pay.from_pay = "Visa Gold 944734465095960"
    assert pay.from_pay is None

    pay.from_pay = "Visa Platinum 2256483756A542539"
    assert pay.from_pay is None

    pay.from_pay = "Счет E97584898735659638967"
    assert pay.from_pay is None

    pay.from_pay = "Visa Gold 9758489873566301020067"
    assert pay.from_pay is None

    pay.from_pay = "Счет 9758489873566301020067"
    assert pay.from_pay is None

    pay.from_pay = "Счет 9758489873566367"
    assert pay.from_pay is None


def test_to_pay_correct(pay):
    pay.to_pay = "Maestro 4598300720424501"
    assert pay.to_pay == ("Maestro", "4598300720424501")

    pay.to_pay = "Visa Gold 9447344650495960"
    assert pay.to_pay == ("Visa Gold", "9447344650495960")

    pay.to_pay = "Счет 97584898735659638967"
    assert pay.to_pay == ("Счет", "97584898735659638967")


def test_to_pay_incorrect(pay):
    pay.to_pay = "Maestro4598300720424501"
    assert pay.to_pay is None

    pay.to_pay = "Maestro-4598300720424501"
    assert pay.to_pay is None

    pay.to_pay = "Visa-Gold-944734465095960"
    assert pay.to_pay is None

    pay.to_pay = 4598300720424501
    assert pay.to_pay is None

    pay.to_pay = True
    assert pay.to_pay is None

    pay.to_pay = "Visa Gold 944734465095960"
    assert pay.to_pay is None

    pay.to_pay = "Visa Platinum 2256483756A542539"
    assert pay.to_pay is None

    pay.to_pay = "Счет E97584898735659638967"
    assert pay.to_pay is None

    pay.to_pay = "Visa Gold 9758489873566301020067"
    assert pay.to_pay is None

    pay.to_pay = "Счет 9758489873566301020067"
    assert pay.to_pay is None

    pay.to_pay = "Счет 9758489873566367"
    assert pay.to_pay is None
