import math

def find_next_square(sq):
    n = math.sqrt(sq)
    if n % 1 != 0:
        return -1
    
    return (n+1) ** 2