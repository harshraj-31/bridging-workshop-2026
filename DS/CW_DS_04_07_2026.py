# C1) Fibonacci Series using Recursion

# Recursive function to find nth Fibonacci number
def fibonacci(n):
    if n == 0:
        return 0          # Base case
    elif n == 1:
        return 1          # Base case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Input
n = int(input("Enter number of terms: "))

print("Fibonacci Series:")
for i in range(n):
    print(fibonacci(i), end=" ")

# C2) Binary Search using Recursion

# Recursive function for binary search
def binary_search(arr, low, high, key):

    # Check if search space is valid
    if low <= high:

        # Find middle element
        mid = (low + high) // 2

        # Key found
        if arr[mid] == key:
            return mid

        # Search left half
        elif key < arr[mid]:
            return binary_search(arr, low, mid - 1, key)

        # Search right half
        else:
            return binary_search(arr, mid + 1, high, key)

    # Key not found
    return -1


# Sorted list
arr = [10, 20, 30, 40, 50, 60, 70]

key = int(input("Enter element to search: "))

result = binary_search(arr, 0, len(arr)-1, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")


# C3) Multiplication using Recursive Addition

# Recursive function
def multiply(a, b):

    # Base case
    if b == 0:
        return 0

    # Recursive case
    return a + multiply(a, b - 1)

# Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Multiplication =", multiply(a, b))