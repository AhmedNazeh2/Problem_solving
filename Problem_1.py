#  You are given a list of integers,
#  and you need to write a function that finds all the pairs of numbers whose sum equals a given target sum.
#  The pairs should not include the same number twice, and pairs should not be repeated in the result.

# numbers = [2, 4, 3, 5, 7, 8, -1]
# target_sum = 7


# Objective:
# Return the pairs of numbers whose sum equals 7

# Solution without external libraries:

def find_pairs_with_sum(numbers, target_sum):
    # List to store pairs
    pairs = []
    
    # Use nested loops to check every possible pair
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # If the sum of the two numbers equals the target sum
            if numbers[i] + numbers[j] == target_sum:
                # Add the pair to the list
                pairs.append((numbers[i], numbers[j]))
    
    return pairs

# Example usage
numbers = [2, 4, 3, 5, 7, 8, -1]
target_sum = 7
result = find_pairs_with_sum(numbers, target_sum)

print('=======================================')
print("Solution ==>", result)
print('=======================================')

