from scr.main import main as m
import pytest


@pytest.fixture
def needs():
    return m.PATH, m.COUNT_TRANSFERS, m.OBLIGATION_PARAMETERS_PAY


@pytest.fixture
def needs():
    return m.PATH, m.COUNT_TRANSFERS, m.OBLIGATION_PARAMETERS_PAY


def test_main_correct():
    assert m.main() is None


def test_main_incorrect():
    pass