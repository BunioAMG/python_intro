# my_awesome_lib

A simple Python library for working with lists, text, and numbers.

## Installation
```bash
pip install -e .
```

## Modules
- `data_utils`: praca z listami (flatten, unique elements, dzielenie na porcje)
- `math_tools`: funkcje matematyczne (silnia, liczby pierwsze, ciąg Fibonacciego)
- `text_processing`: analiza tekstu (liczenie słów, odwracanie, usuwanie interpunkcji)

## Usage example

```python
from my_awesome_lib.data_utils import flatten_list, unique_elements, chunk_list

print(flatten_list([[1, 2], [3]]))          # [1, 2, 3]
print(unique_elements([1, 2, 2, 3]))        # [1, 2, 3]
print(chunk_list([1, 2, 3, 4], 2))          # [[1, 2], [3, 4]]
```

```python
from my_awesome_lib.math_tools import factorial, is_prime, fibonacci

print(factorial(5))     # 120
print(is_prime(7))      # True
print(fibonacci(6))     # 8
```

```python
from my_awesome_lib.text_processing import count_words, reverse_words, remove_punctuation

print(count_words("Hello world!"))                   # 2
print(reverse_words("Hello world!"))                 # "world! Hello"
print(remove_punctuation("Hello, world!"))           # "Hello world"
```

## Autor
Patryk Buńkowski – 2025
