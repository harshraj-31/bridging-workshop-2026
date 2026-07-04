#Homework 
# H1) Generate all 3-digit lock combinations
# Digits: 1,2,3
# No repetitions

# Recursive function
def generate(current, used):

    # If combination has 3 digits
    if len(current) == 3:
        print(current)
        return

    # Try each digit
    for digit in ['1', '2', '3']:

        # Skip already used digit
        if digit not in used:
            generate(current + digit, used + [digit])

# Start recursion
generate("", [])

# H2) Folder Size Calculator

# Recursive function
def folder_size(folder):

    total = 0

    for item in folder:

        # If item is another folder (dictionary)
        if isinstance(item, dict):
            total += folder_size(item)

        # Otherwise it is a file
        else:
            total += item

    return total


# Example folder structure
folder = {
    "file1": 100,
    "file2": 250,
    "folder1": {
        "file3": 300,
        "file4": 150
    },
    "folder2": {
        "file5": 500
    }
}

print("Total Folder Size =", folder_size(folder))


# H3) Number of Ways to Climb Stairs

# Recursive function
def climb(n):

    # Base cases
    if n == 0 or n == 1:
        return 1

    # Recursive relation
    return climb(n - 1) + climb(n - 2)

# Input
n = int(input("Enter number of stairs: "))

print("Number of ways =", climb(n))
