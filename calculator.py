import math

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a and b, raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def exponentiate(base, exponent):
    """Return the result of base raised to the power of exponent."""
    return base ** exponent

def square_root(a):
    """Return the square root of a, raises ValueError if a is negative."""
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number")
    return math.sqrt(a)

if __name__ == "__main__":
    print("Basic Calculator is ready!")

