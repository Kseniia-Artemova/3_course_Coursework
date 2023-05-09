import scr.main as m
import pytest


def test_main_correct():
    assert m.main() is None


def test_main_incorrect_path():
    m.PATH = "operations.json"
    with pytest.raises(FileNotFoundError):
        m.main()
