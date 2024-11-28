def camel_to_snake(camel):
    """Convert camel case string to snake case."""
    snake = ""  # Initialized empty string, serves as a container to build the output string in snake case step by step
    for c in camel:
        if c.isupper():  # Check if the character is uppercase
            snake += "_" + c.lower()  # Add an underscore and the lowercase version
        else:
            snake += c  # Append the character as it is
    return snake.lstrip("_")  # Remove any leading underscore


def main():
    camel_case = input("Enter a camel case variable: ")
    snake_case = camel_to_snake(camel_case)
    print("The variable in snake case is:", snake_case)


if __name__ == "__main__":
    main()
