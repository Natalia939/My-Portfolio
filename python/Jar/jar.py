class Jar:
    # Initialize the Jar class with a default capacity of 12 cookies
    def __init__(self, capacity=12):
        # Ensure the capacity is a non-negative integer; raise ValueError if not
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self.capacity = capacity  # Set the maximum number of cookies the jar can hold
        self._cookies = 0  # Private variable to track the current number of cookies

    # Define the string representation of the jar
    def __str__(self):
        # Display cookies as "🍪" for the current number in the jar
        return "🍪" * self._cookies

    # Method to add cookies to the jar
    def deposit(self, n):
        # Validate input: n must be a non-negative integer
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies must be a non-negative integer.")
        # Ensure the jar has enough capacity for the cookies being added
        if self._cookies + n > self.capacity:
            raise ValueError("Not enough space in the jar.")
        self._cookies += n  # Add the cookies to the jar

    # Method to remove cookies from the jar
    def withdraw(self, n):
        # Validate input: n must be a non-negative integer
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies must be a non-negative integer.")
        # Ensure there are enough cookies to remove
        if n > self._cookies:
            raise ValueError("Not enough cookies in the jar to withdraw.")
        self._cookies -= n  # Subtract the cookies from the jar

    # Property to return the current number of cookies in the jar
    @property
    def size(self):
        return self._cookies
