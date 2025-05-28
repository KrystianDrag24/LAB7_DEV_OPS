from calculator import dodawanie
import pytest

def test_dodawanie():
    assert dodawanie(2, 3) == 5
    assert dodawanie(-1, 1) == 0