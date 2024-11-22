import bank


def test_hello():
    # Test greetings starting with "hello"
    assert bank.value("hello") == 0
    assert bank.value("Hello") == 0
    assert bank.value("HELLO there!") == 0


def test_h_but_not_hello():
    # Test greetings starting with "h" but not "hello"
    assert bank.value("hi") == 20
    assert bank.value("Hey") == 20
    assert bank.value("Holla!") == 20


def test_other_greetings():
    # Test greetings that do not start with "h"
    assert bank.value("good morning") == 100
    assert bank.value("Goodbye") == 100
    assert bank.value("What's up?") == 100


def test_edge_cases():
    # Test edge cases
    assert bank.value("h") == 20
    assert bank.value("hellohello") == 0
    assert bank.value("HELLOworld") == 0
