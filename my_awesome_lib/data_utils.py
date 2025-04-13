def flatten_list(nested_list):
    """Flatten a list of lists into a single list."""
    return [item for sublist in nested_list for item in sublist]

def unique_elements(data):
    """Return a list of unique elements from the input list."""
    return list(set(data))

def chunk_list(data, chunk_size):
    """Divide a list into chunks of specified size."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]