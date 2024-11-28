def main():
    # Prompt the user for a greeting
    greeting = input("Greeting: ").strip()

    # Get the value based on the greeting
    result = value(greeting)

    # Print the result
    print(f"${result}")


def value(greeting):
    """
    Determine the value based on the greeting.
    Returns:
        0 if the greeting starts with "hello",
        20 if it starts with "h" (but not "hello"),
        100 otherwise.
    """
    greeting = greeting.lower()  # Make the greeting case-insensitive

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
