def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check divisors up to square root of n
    max_divisor = int(n**0.5) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
    return True

# Get user input
user_input = int(input("Enter a number to check if it's prime: "))

# Check and display result
if is_prime(user_input):
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")