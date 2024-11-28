import random


def main():
    level = get_positive_integer("Level: ")  # Prompt for level
    number = random.randint(1, level)        # Generate random number
    while True:
        guess = get_positive_integer("Guess: ")  # Prompt for guess
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break


def get_positive_integer(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass  # Ignore invalid input and prompt again


if __name__ == "__main__":
    main()
