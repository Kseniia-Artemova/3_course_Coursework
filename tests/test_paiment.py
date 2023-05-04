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


