from seasons import get_dob
import pytest


def main():
    test_format()
    test_year()
    test_month()
    test_day()


def test_format():
    assert get_dob("2020-12-20").year == 2020
    assert get_dob("2020-12-20").month == 12
    assert get_dob("2020-12-20").day == 20
    with pytest.raises(SystemExit):
        get_dob("20-12-2020")  # D-M-Y
    with pytest.raises(SystemExit):
        get_dob("2020-20-12")  # Y-D-M
    with pytest.raises(SystemExit):
        get_dob("12-20-2020")  # M-D-Y
    with pytest.raises(SystemExit):
        get_dob("12-2020-20")  # M-Y-D


def test_year():
    assert get_dob("0001-1-1").year == 1
    assert get_dob("1111-1-1").year == 1111
    assert get_dob("5555-1-1").year == 5555
    assert get_dob("9999-1-1").year == 9999
    with pytest.raises(SystemExit):
        get_dob("1-1-1")
    with pytest.raises(SystemExit):
        get_dob("01-1-1")
    with pytest.raises(SystemExit):
        get_dob("001-1-1")
    with pytest.raises(SystemExit):
        get_dob("10000-1-1")


def test_month():
    assert get_dob("1111-1-1").month == 1
    assert get_dob("1111-12-1").month == 12
    with pytest.raises(SystemExit):
        get_dob("1111-13-1")
    with pytest.raises(SystemExit):
        get_dob("1111-20-1")


def test_day():
    assert get_dob("1111-1-1").day == 1
    assert get_dob("1111-1-30").day == 30
    with pytest.raises(SystemExit):
        get_dob("1111-1-35")
    with pytest.raises(SystemExit):
        get_dob("1111-1-50")


if __name__ == "__main__":
    main()
