def main():
    # Prompt the user for a time
    time = input("What time is it? ").strip()

    # Convert the time to a float
    hours = convert(time)

    # Check which meal time it is
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")


def convert(time):
    """
    Converts a time string in 24-hour format to a float.
    For example: "7:30" becomes 7.5, "18:15" becomes 18.25.
    """
    # Split the time into hours and minutes
    hours, minutes = map(int, time.split(":"))

    # Convert to float (hours + fraction of an hour)
    return hours + minutes / 60


if __name__ == "__main__":
    main()
