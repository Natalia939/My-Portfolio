def main():
    # Dictionary of fruits and their calories
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80,
    }

    # Prompt the user for a fruit (case-insensitively)
    fruit = input("Fruit: ").strip().lower()

    # Check if the fruit is in the dictionary and output its calories
    if fruit in fruit_calories:
        print(f"Calories: {fruit_calories[fruit]}")
    # Ignore input that is not a fruit
    else:
        pass


if __name__ == "__main__":
    main()
