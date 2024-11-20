def main():
    # Define the total cost of the Coke
    cost = 50
    amount_due = cost

    # Keep prompting the user until the amount due is zero or less
    while amount_due > 0:
        # Prompt the user to insert a coin
        try:
            coin = int(input("Insert Coin: "))
        except ValueError:
            # If the user enters something invalid, ignore it
            continue

        # Accept only valid coins: 25, 10, 5
        if coin in [25, 10, 5]:
            amount_due -= coin  # Deduct the coin from the amount due

        # Output the current amount due if greater than zero
        if amount_due > 0:
            print(f"Amount Due: {amount_due}")

    # Calculate and display change owed (if any)
    print(f"Change Owed: {abs(amount_due)}")

if __name__ == "__main__":
    main()
