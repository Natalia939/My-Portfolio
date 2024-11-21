def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length requirements
    if not (2 <= len(s) <= 6):
        return False

    # Check that it starts with at least two letters
    if not s[:2].isalpha():
        return False

    # Check for invalid characters
    if not s.isalnum():  # Ensures no punctuation, spaces, or periods
        return False

    # Check number placement
    number_found = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not number_found:
                # First digit cannot be 0
                if char == '0':
                    return False
                number_found = True
            else:
                # Numbers must remain at the end
                if not s[i:].isdigit():
                    return False

    return True


if __name__ == "__main__":
    main()
