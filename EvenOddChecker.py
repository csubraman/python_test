# EvenOddChecker.py

def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

def check_list(numbers):
    results = []
    for num in numbers:
        results.append(check_even_odd(num))
    return results

# --- Part 1: Check single number ---
try:
    user_input = int(input("Enter a number to check if it's Even or Odd: "))
    print(check_even_odd(user_input))
except ValueError:
    print("Invalid input. Please enter an integer.")

# --- Part 2: Check list of numbers ---
print("\nChecking a list of numbers [10, 15, 22, 33, 44]:")
number_list = [10, 15, 22, 33, 44]
for result in check_list(number_list):
    print(result)
