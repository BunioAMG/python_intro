import re  # Import regular expressions for email validation
from datetime import datetime  # Import datetime to work with dates



# 1. Function: is_valid_email
def is_valid_email(email):
    """
    Validates if the given email is in a correct format.
    """
    # Uses a regex pattern: checks if there is some text before/after "@" and a domain
    return re.match(r"^[^@]+@[^@]+\.[^@]+$", email) is not None


# 2. Function: calculate_rectangle_area
def calculate_rectangle_area(width, height):
    """
    Calculates the area of a rectangle.
    Raises ValueError if width or height is negative.
    """
    if width < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")  # Raise error for negative dimensions
    return width * height  # Return calculated area


# 3. Function: filter_even_numbers
def filter_even_numbers(numbers):
    """
    Filters even integers from the input list.
    Ignores non-integer types.
    """
    return [n for n in numbers if isinstance(n, int) and n % 2 == 0]


# 4. Function: convert_date_format
def convert_date_format(date_str):
    """
    Converts a date from 'YYYY-MM-DD' to 'DD.MM.YYYY'.
    Raises ValueError for invalid dates or formats.
    """
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")  # Parse string into date object
        return date.strftime("%d.%m.%Y")  # Format the date into desired output
    except ValueError:
        raise ValueError("Invalid date format")  # Raise error if parsing fails


# 5. Function: is_palindrome
def is_palindrome(text):
    """
    Checks if the given text is a palindrome (ignoring case and spaces).
    """
    cleaned = ''.join(c.lower() for c in text if c.isalnum())  # Lowercase and keep only letters/digits
    return cleaned == cleaned[::-1]  # Compare the string with its reverse


