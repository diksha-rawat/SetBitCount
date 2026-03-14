def countsetbit(start, end=None):
    """
    Count set bits in a single number or a range of natural numbers.
    
    Args:
        start (int): A single number OR start of range
        end   (int): End of range (optional)
    
    Returns:
        int: Total count of set bits
    
    Examples:
        countsetbit(3)     → 2
        countsetbit(1, 7)  → 12
    """
    # Validate inputs are integers
    if not isinstance(start, int):
        raise TypeError(f"Expected int, got {type(start).__name__}")
    
    if end is not None and not isinstance(end, int):
        raise TypeError(f"Expected int, got {type(end).__name__}")

    # Validate no negative numbers
    if start < 0:
        raise ValueError("start must be a non-negative integer")
    
    if end is not None and end < 0:
        raise ValueError("end must be a non-negative integer")

    # Validate range is correct
    if end is not None and end < start:
        raise ValueError(f"end ({end}) must be greater than or equal to start ({start})")

    # Count set bits in a single number
    if end is None:
        return bin(start).count('1')

    # Count set bits in a range
    return sum(bin(i).count('1') for i in range(start, end + 1))
