from jar import Jar  # Import the Jar class from jar.py
import pytest  # Import pytest for testing

# Test the initialization of the Jar class


def test_init():
    # Create a jar with default capacity (12 cookies)
    jar = Jar()
    assert jar.capacity == 12  # Verify the default capacity is 12
    assert jar.size == 0  # Verify the jar is empty upon initialization

    # Test invalid initialization (negative capacity)
    with pytest.raises(ValueError):  # Expect a ValueError to be raised
        Jar(-1)  # Attempt to create a jar with a negative capacity

# Test the string representation of the jar


def test_str():
    jar = Jar(5)  # Create a jar with a capacity of 5 cookies
    jar.deposit(3)  # Add 3 cookies to the jar
    assert str(jar) == "🍪🍪🍪"  # Verify the string representation matches the number of cookies
    jar.withdraw(1)  # Remove 1 cookie from the jar
    assert str(jar) == "🍪🍪"  # Verify the updated string representation

# Test the deposit method


def test_deposit():
    jar = Jar(5)  # Create a jar with a capacity of 5 cookies
    jar.deposit(3)  # Add 3 cookies
    assert jar.size == 3  # Verify the jar now contains 3 cookies

    # Test exceeding capacity
    with pytest.raises(ValueError):  # Expect a ValueError if overfilling the jar
        jar.deposit(3)  # Attempt to add 3 more cookies (exceeds capacity)

# Test the withdraw method


def test_withdraw():
    jar = Jar(5)  # Create a jar with a capacity of 5 cookies
    jar.deposit(4)  # Add 4 cookies to the jar
    jar.withdraw(2)  # Remove 2 cookies
    assert jar.size == 2  # Verify the jar now contains 2 cookies

    # Test withdrawing more cookies than available
    with pytest.raises(ValueError):  # Expect a ValueError if removing too many cookies
        jar.withdraw(5)  # Attempt to withdraw 5 cookies (not enough in the jar)
