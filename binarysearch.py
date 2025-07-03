# Binary Search Function
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Find the middle index

        if arr[mid] == target:
            return mid  # Target found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1  # Target not found

# Example usage
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # List must be sorted
target = int(input("Enter the number to search: "))

result = binary_search(numbers, target)

if result != -1:
    print(f"{target} found at position {result + 1}")  # +1 for human-friendly position
else:
    print(f"{target} not found in the list.")
