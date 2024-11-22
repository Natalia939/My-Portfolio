def main():
    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError):
        print("Invalid input")


def convert(fraction):
    """
    Convert a fraction string (X/Y) to a percentage.
    Raise ValueError if X and/or Y are not integers or if X > Y.
    Raise ZeroDivisionError if Y == 0.
    """
    try:
        x, y = map(int, fraction.split("/"))
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        return round((x / y) * 100)
    except (ValueError, ZeroDivisionError):
        raise


def gauge(percentage):
    """
    Return:
    - "E" if percentage <= 1
    - "F" if percentage >= 99
    - "Z%" otherwise, where Z is the percentage
    """
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

