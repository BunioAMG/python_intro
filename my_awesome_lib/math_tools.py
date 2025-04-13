def factorial(n):
    """Calculate factorial of a number."""
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    """Check if a number is a prime."""
    if not isinstance(n, int) or n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    """Return the nth Fibonacci number."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Fibonacci is only defined for non-negative integers")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

