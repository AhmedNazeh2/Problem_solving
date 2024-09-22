# find_missing_number

def find_missing_number(arr, n):
    total = (n * (n + 1)) // 2  # Calculate the expected sum ==> total = 36
    return total - sum(arr)      # Calculate the missing number ==> sum(arr) = 31

           # permission == 36 - 31 = 5 

# Example
arr = [1, 2, 4, 6, 3, 7, 8]
n = 8
print(find_missing_number(arr, n))  # Output: 5
