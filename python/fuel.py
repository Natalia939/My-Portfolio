def main():
    while True:
        try:
            # Prompt user for a fraction
            fraction = input("Fraction: ").strip()

            # Split the fraction into X and Y
            x, y = map(int, fraction.split("/"))

            # Validate that Y is not zero and X is not greater than Y
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError

            # Calculate the percentage
            percentage = round((x / y) * 100)

            # Output based on the percentage
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")

            break  # Exit the loop after successful input and output

        except (ValueError, ZeroDivisionError):
            # Handle invalid input and prompt again
            pass


if __name__ == "__main__":
    main()
