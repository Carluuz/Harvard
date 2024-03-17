import pytest
from project import get_valid_input, get_inputs


def test_get_valid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: '1')
    assert get_valid_input("Enter a number: ") == 1
    monkeypatch.setattr('builtins.input', lambda x: '5')
    assert get_valid_input("Enter a number: ") == 5
    monkeypatch.setattr('builtins.input', lambda x: '100')
    assert get_valid_input("Enter a number: ") == 100

def test_get_inputs(monkeypatch):
    inputs = iter(['1', '2'])
    monkeypatch.setattr('builtins.input', lambda x: next(inputs))
    assert get_inputs() == (1, 2)
    inputs = iter(['10', '20'])
    monkeypatch.setattr('builtins.input', lambda x: next(inputs))
    assert get_inputs() == (10, 20)
    inputs = iter(['100', '200'])
    monkeypatch.setattr('builtins.input', lambda x: next(inputs))
    assert get_inputs() == (100, 200)
