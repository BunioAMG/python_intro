def count_words(text):
    """Return the number of words in the text."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return len(text.split())

def reverse_words(text):
    """Return a string with the words reversed."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return ' '.join(text.split()[::-1])

def remove_punctuation(text):
    """Remove common punctuation from the text."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    import string
    return text.translate(str.maketrans('', '', string.punctuation))
