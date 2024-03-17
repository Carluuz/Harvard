from um import count
import re

def main():
    test_no_um()
    test_single_um()
    test_multiple_um()


def test_no_um():
    assert count("no regex") == 0
    assert count("Hum, thanks") == 0

def test_single_um():
    assert count("1 um regex") == 1
    assert count("um regex") == 1
    assert count("Um regex") == 1
    assert count("1 regex um") == 1


def test_multiple_um():
    assert count("2 um um regex") == 2
    assert count("3 um um um regex") == 3
    assert count("4 um um um um regex") == 4



