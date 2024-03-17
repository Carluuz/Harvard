from jar import Jar
import pytest


def test_init():
    jar = Jar()


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(1)
    assert str(jar) == "🍪🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.deposit(20)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    assert jar.size == 10
    jar.withdraw(5)
    assert jar.size == 5
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(20)

def test_capacity():
    jar = Jar()
    assert jar.capacity == 12


def test_size():
    jar = Jar()
    assert jar.size == 0
