# Palindrome Check
# Task: Write a function that checks if a given string is a palindrome.

# Explanation: A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

def is_palindrome(s):
    # Normalize the string
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

# Example usage
phrase = "A man, a plan, a canal, Panama!"
print(f"Is the phrase '{phrase}' a palindrome? {is_palindrome(phrase)}") # Is the phrase 'A man, a plan, a canal, Panama!' a palindrome? True
