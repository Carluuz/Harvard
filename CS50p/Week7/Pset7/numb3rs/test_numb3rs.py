import re
import sys
from numb3rs import validate

def main():
    test_valid()
    test_negatives()
    test_over()
    test_str()
    test_less_and_more_n()

def test_valid():
    assert validate("1.2.3.4") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True


def test_negatives():
    assert validate("-1.2.3.4") == False
    assert validate("1.-2.3.4") == False
    assert validate("1.2.-3.4") == False
    assert validate("1.2.3.-4") == False
    assert validate("-1.-2.-3.-4") == False
    assert validate("--255.-255.-255.-255") == False

def test_over():
    assert validate("256.2.3.4") == False
    assert validate("1.256.3.4") == False
    assert validate("1.2.256.4") == False
    assert validate("1.2.3.256") == False
    assert validate("256.256.256.256") == False


def test_str():
    assert validate("cat") == False
    assert validate("dog") == False


def test_less_and_more_n():
    assert validate("1.2.3.4.5.6") == False
    assert validate("1.2.3.4.5") == False
    assert validate("1.2.3.4") == True
    assert validate("1.2.3") == False
    assert validate("1.2") == False
    assert validate("1") == False


if __name__ == "__main__":
    main()
