import sys
import requests


def main():
    # Ensure the user provides a valid number of Bitcoins as a command-line argument
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])  # Convert the argument to a float
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Fetch the current Bitcoin price in USD
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Parse the JSON response
        rate = data["bpi"]["USD"]["rate_float"]  # Extract the USD rate as a float
    except requests.RequestException:
        sys.exit("Error: Unable to fetch Bitcoin price.")
    except KeyError:
        sys.exit("Error: Unexpected response structure.")

    # Calculate the total cost and display it
    total_cost = bitcoins * rate
    print(f"${total_cost:,.4f}")


if __name__ == "__main__":
    main()
