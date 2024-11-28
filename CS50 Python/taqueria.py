def main():
    # Define the menu
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0.0  # Initialize total cost

    while True:
        try:
            # Prompt the user for an item
            item = input("Item: ").strip().title()

            # Check if the item is in the menu
            if item in menu:
                total += menu[item]
                print(f"${total:.2f}")  # Display running total
            else:
                # Ignore invalid items
                continue

        except EOFError:
            # Exit on Ctrl+D
            print()  # Print a newline for clean output
            break


if __name__ == "__main__":
    main()
