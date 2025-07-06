# Filename: AgeCategory.py

"""
This script prompts the user for an age and determines if the person is a
child, teenager, adult, or senior. It includes error handling for invalid input.
"""

def get_age_category(age: int) -> str:
    """
    Determines the age category based on the provided age.

    The categories are defined as:
    - Child: 0 - 12
    - Teenager: 13 - 19
    - Adult: 20 - 64
    - Senior: 65 and over

    Args:
        age (int): The age of the person.

    Returns:
        str: The corresponding age category string, or an error message for invalid ages.
    """
    if age < 0:
        return "Invalid Age: Age cannot be negative."
    elif age <= 12:
        return "Child"
    elif age <= 19:
        # This block is only reached if age is greater than 12
        return "Teenager"
    elif age <= 64:
        # This block is only reached if age is greater than 19
        return "Adult"
    else:
        # This block is for any age 65 and over
        return "Senior"

# This is the main part of the script that runs when you execute the file
if __name__ == "__main__":
    try:
        # 1. Prompt the user for input and store it as a string
        age_input = input("Please enter an age: ")

        # 2. Convert the input string to an integer.
        #    This will raise a ValueError if the input is not a whole number.
        user_age = int(age_input)

        # 3. Get the category by calling our function
        category = get_age_category(user_age)

        # 4. Print the final, formatted result
        print(f"An age of {user_age} falls into the '{category}' category.")

    except ValueError:
        # This block runs if int(age_input) fails because the user entered text
        print(f"Error: Invalid input. '{age_input}' is not a whole number. Please run the script again.")