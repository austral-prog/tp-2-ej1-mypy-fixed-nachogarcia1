def max_of_two(x: int, y: int) -> int:
    """Given x and y, that are 2 numbers, return the biggest number."""
    biggest: int = x
    if x >= y:
        return biggest
    else:
        biggest: int = y
        return biggest

def max_of_three(x: int, y: int, z: int) -> int:
    biggest: int = x
    if x > y and x > z:
        biggest = x
    elif y > x and y > z:
        biggest = y
    else:
        biggest = z
    return biggest
