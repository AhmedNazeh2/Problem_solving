# Sum of Digits
# Task: Write a function that returns the sum of the digits of a number.

# Explanation: To find the sum of the digits, convert the number to a string, iterate over each character, convert it back to an integer, and sum them up.

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Example usage
number = 12345
print(f"The sum of the digits of {number} is {sum_of_digits(number)}") # The sum of the digits of 12345 is 15
