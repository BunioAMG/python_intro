PYTHON TDD PROJECT – UNIT TESTING WITH unittest

----------------------------------------
PROJECT STRUCTURE
----------------------------------------

app.py           # Application functions

test_app.py      # Unit tests using unittest

README.txt       # Project description

----------------------------------------
FUNCTIONS INCLUDED (IN app.py)
----------------------------------------

1. is_valid_email(email)
   - Validates if the input string is a properly formatted email address.

2. calculate_rectangle_area(width, height)
   - Returns the area of a rectangle.
   - Raises ValueError if width or height is negative.

3. filter_even_numbers(numbers)
   - Filters and returns only even integers from a list.
   - Ignores non-integer types.

4. convert_date_format(date_str)
   - Converts a date from 'YYYY-MM-DD' to 'DD.MM.YYYY'.
   - Raises ValueError for invalid formats or dates.

5. is_palindrome(text)
   - Checks if the text is a palindrome.
   - Ignores spaces and letter casing.

----------------------------------------
RUNNING TESTS
----------------------------------------

Use the following command to run all tests:

    python test_app.py

Expected output:

    ..................................................................
    ------------------------------------------------------------------
    Ran all tests successfully.

----------------------------------------
TEST COVERAGE REPORT
----------------------------------------

Name          Stmts   Miss  Cover   Missing
-------------------------------------------
app.py           19      0   100%
test_app.py      59      0   100%
-------------------------------------------
TOTAL            78      0   100%



