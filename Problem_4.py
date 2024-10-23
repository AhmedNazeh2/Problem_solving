# Prime Number Check
# Task: Write a function that checks if a number is prime.

# Explanation: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
number = 29
print(f"{number} is prime: {is_prime(number)}")  # 29 is prime: True
