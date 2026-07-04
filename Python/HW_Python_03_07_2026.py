#word frequency counter
def word_frequency(paragraph):
    # Convert to lowercase and remove punctuation
    cleaned = ""
    for char in paragraph:
        if char.isalnum() or char.isspace():
            cleaned += char.lower()
        else:
            cleaned += " "
    
    # Split into words
    words = cleaned.split()
    
    # Count frequency using a dictionary
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    
    return freq


# Example usage
paragraph = """Python is a great programming language. Python is easy to learn, 
and Python is widely used for data science, web development, and automation."""

result = word_frequency(paragraph)

# Print the results
for word, count in sorted(result.items(), key=lambda x: -x[1]):
    print(f"{word}: {count}")


#palindrome checker using string
def is_palindrome(s):
    # Remove spaces and convert to lowercase for accurate comparison
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned += char.lower()
    
    # Compare the string with its reverse
    return cleaned == cleaned[::-1]


# Example usage
test_strings = ["madam", "hello", "A man a plan a canal Panama", "Python"]

for s in test_strings:
    if is_palindrome(s):
        print(f'"{s}" is a palindrome')
    else:
        print(f'"{s}" is NOT a palindrome')