from calculator import mnozenie
import pytest

def test_mnozenie():
    assert mnozenie(2, 3) == 6
    assert mnozenie(-1, 1) == -1