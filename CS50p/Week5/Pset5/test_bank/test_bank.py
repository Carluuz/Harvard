from bank import value

def main():
    test_no_h()
    test_first_h()
    test_hello()

def test_no_h():
    assert value("hello") == 0
    assert value("  Hello  ") == 0

def test_first_h():
    assert value("hi") == 20
    assert value("how you doing?") == 20
    assert value("  hi  ") == 20

def test_hello():
    assert value("what's happening?") == 100
    assert value("  What's up?  ") == 100

if __name__ == "__main__":
    main()
