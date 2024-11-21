def main():
    grocery_list = {}  # Dictionary to store items and their counts

    while True:
        try:
            # Prompt user for an item
            item = input().strip().lower()

            # Add item to the dictionary or update its count
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1

        except EOFError:
            # End input on Ctrl+D
            print()  # Print a newline for clean output
            break

    # Output the grocery list, sorted alphabetically
    for item in sorted(grocery_list.keys()):
        print(f"{grocery_list[item]} {item.upper()}")


if __name__ == "__main__":
    main()
