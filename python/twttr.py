def main():
    # Prompt the user for input
    text = input("Input: ")

    # Call the function to remove vowels
    result = remove_vowels(text)

    # Print the result
    print(f"Output: {result}")


def remove_vowels(text):
    """
    Removes all vowels (both uppercase and lowercase) from the input text.
    """
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:  # Check if character is not a vowel
            result += char      # Add it to the result
    return result


if __name__ == "__main__":
    main()
