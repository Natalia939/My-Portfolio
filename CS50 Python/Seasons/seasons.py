from datetime import date
import inflect  # Imports the inflect library, which is used to convert numbers into words.
import sys


def main():
    birth_date = input("Date of Birth (YYYY-MM-DD): ")
    minutes = calculate_minutes(birth_date)
    if minutes is not None:
        print(f"{convert_to_words(minutes)} minutes")
    else:
        sys.exit("Invalid date format")


def calculate_minutes(birth_date):
    try:
        birth_date = date.fromisoformat(birth_date)
        today = date.today()
        # Calculates the difference between today's date and the user's birth date.
        delta = today - birth_date
        # Converts the total days into minutes by multiplying by 24 (hours per day) and 60 (minutes per hour).
        return delta.days * 24 * 60
    except ValueError:
        # If the input date is invalid (e.g., not in the YYYY-MM-DD format), the function catches the ValueError and returns None.
        return None


def convert_to_words(minutes):
    # Creates an instance of the inflect engine, which is used to convert numbers to words.
    p = inflect.engine()
    # Converts the numeric value (minutes) into words. The andword="" parameter ensures that the word "and" is omitted (e.g., "One hundred twenty-five" instead of "One hundred and twenty-five").
    return p.number_to_words(minutes, andword="").capitalize()


if __name__ == "__main__":
    main()
