def max_of_two(x: int, y: int) -> int:
    biggest: int = x
    if x >= y:
        return biggest
    else:
        biggest = y
        return biggest

def max_of_three(x: int, y: int, z: int) -> int:
    biggest2: int = x
    if x > y and x > z:
        biggest2 = x
    elif y > x and y > z:
        biggest2 = y
    else:
        biggest2 = z
    return biggest2
